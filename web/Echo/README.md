

# Echo

- 這題在最開始做的時候完全沒有頭緒，看起來是很基本的 express + ejs，這組只有我會打 Web ，於是自己在一旁先發想~~通靈~~可能的漏洞，畢竟 Javascript 有一堆神奇的特性

- Node.js 是近幾年才出現的題目類型，我本來就只知道型別很怪還有原型鍊污染少少的攻擊方式，反正是 Kaibro 出的吧，沒想法就先去看 [小抄](https://github.com/w181496/Web-CTF-Cheatsheet) 還有 [Writeups](https://github.com/w181496/CTF) 還有 [推特](https://twitter.com/kaikaibro)，然而並沒什麼卵用

- 餵狗查了今年有關 CTF 和 js的資訊，只有查到 XNUCA2019 CTF hardjs，原理一樣是利用原型鍊污染，於是我就朝 body-parser.urlencoded 本身是不是有 CVE 造成原型鍊污染，可惜沒有。fuzz 一下是可以弄出 Object 還有覆蓋 toString 等等，但是 Object 下的屬性就修改不到。

- 沒辦法只好去研究 ejs source code（反正其他的題目不會寫）， 我先利用覆蓋 toString 造成渲染模板時出錯，來 backtrace 函式呼叫
。當時只是猜渲染模板應該會用到 toString，後來看官方文檔上有寫 ![](https://i.imgur.com/eh9IfB7.png)

- 在 ejs 注入一堆 console.log 後才讀懂整個模板語言的流程，大致上是 
    1. express render 底層會呼叫 ejs 的 renderFile，先處理 data、options、callback，為了相容 Express 2，出現可以把 options 寫在 data 的奇怪 feature，
    ```
    // Undocumented after Express 2, but still usable, esp. for
        // items that are unsafe to be passed along with data, like `root`
        viewOpts = data.settings['view options'];
        if (viewOpts) {
          utils.shallowCopy(opts, viewOpts);
        }
      }
      // Express 2 and lower, values set in app.locals, or people who just
      // want to pass options in their data. NOTE: These values will override
      // anything previously set in settings  or settings['view options']
      utils.shallowCopyFromList(opts, data, _OPTS_PASSABLE_WITH_DATA_EXPRESS);
    }
    opts.filename = filename;
    ```
    ，且因為他的實做會把 data 的東東複製到 options，前面直接傳入 req.body 的方式讓我們可以污染 options。我一開始只有注意到下半部 _OPTS_PASSABLE_WITH_DATA_EXPRESS 限制了可傳入 options，一直試著在有限的 options 裡找解法，其實上半部傳入 'view options' 就直接解除所有限制 Orz
    2. ejs 在處理完 data、 options 後會實例化一個 Template 類，然後透過 parse 原本 .ejs 文件來產生 "產生渲染後的模板" 的函式。 hardjs 那題就是利用產生 "產生渲染後的模板" 時的 feature，
    ![](https://i.imgur.com/YYMyjBz.png)
    只要能污染 outputFunctionName，就能注入任意指令。
    ```
    if (!this.source) {
      this.generateSource();
      prepended += '  var __output = [], __append = __output.push.bind(__output);' + '\n';
      if (opts.outputFunctionName) {
        prepended += '  var ' + opts.outputFunctionName + ' = __append;' + '\n';
      }
      if (opts._with !== false) {
        prepended +=  '  with (' + opts.localsName + ' || {}) {' + '\n';
        appended += '  }' + '\n';
      }
    ```
    outputFunctionName 並不在 _OPTS_PASSABLE_WITH_DATA_EXPRESS 裡，所以理論是不希望開發者傳入污染到才對，可是結合前一個 feature 就 bypass 了。
    
    3. 撰寫 payload 時要注意閉合前後，還有他是用`Function`類來創造函式，執行方式類似 `eval` 的樣子，會沒辦法直接 `require` 和接觸 app.js 裡的 fs，查到一種方式是用 `global.process.mainModule.constructor._load('fs')` 來載入 `fs`
    4. 最後的 payload: `settings[view+options][outputFunctionName]=a%3B__append(global.process.mainModule.constructor._load('fs').readFileSync('%2Fflag'))%3Ba`
    5. FLAG{I_th1nk_cyku_i5_0ur_w3b_g0d}
- 其他心得
    -  做完這題感覺超可怕，參數裡甚至不用放 text，所以只要直接或是間接把使用者資料傳入就造成 RCE，這樣算是很大的漏洞還是使用者習慣不佳呢？
    - settings 裡還可以控制模板的開閉合標籤，如果 ejs 模板出現 `ab_cba`的結構就可以 eval c 達成 RCE，這串有可能會在變數取名時出現，也許某天有用？
    
