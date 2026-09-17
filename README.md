# Exercise 1 實作教學

這次實作會透過一支簡單的待辦清單 CLI 程式，練習 Git、GitHub 與 uv 的基本操作。

## Phase 1：建立專案環境

1. 開範例 repo：[https://github.com/GeorgeShiue/intro-to-csie-exercise-1](https://github.com/GeorgeShiue/intro-to-csie-exercise-1)，點頁面右上角綠色的 **Use this template** 按鈕 → 選 **Create a new repository**，建立自己的 repo
   - 這一步是把這個範例 repo 當「模板」，複製一份獨立的新 repo 到你自己的 GitHub 帳號底下（有自己的 commit 歷史，跟原本的範例 repo 沒有關聯）。這跟 fork 不同：fork 會保留與原 repo 的關聯，template 則不會，適合當作個人作業的起點
   - 依畫面指示輸入 repo 名稱，選擇 Public，按 **Create repository**
2. 在自己電腦上，把 repo clone 到本機資料夾：
   - **VS Code**：按 `Cmd+Shift+P`（Windows/Linux 是 `Ctrl+Shift+P`）打開命令面板，輸入並選擇 **Git: Clone** → 貼上自己 repo 的網址 → 選擇要存放的本機資料夾
   - **終端機**：先到自己的 GitHub repo 頁面，點右上角綠色的 **Code** 按鈕，複製 HTTPS 網址（例如 `https://github.com/<你的帳號>/<repo 名稱>.git`），再執行：

     ```bash
     git clone <剛剛複製的網址>
     ```
3. 用 VS Code 開啟這個資料夾，在內建終端機執行 `uv init`（可加 `--python 3.14` 指定版本），**在寫任何程式之前先把專案的環境準備好**
   - 這一步會產生：`pyproject.toml`（宣告這個專案用什麼 Python 版本、之後會裝什麼套件）、`.python-version`。因為資料夾裡已經有 `README.md`，uv 會把這個專案當成一個「package」來初始化，所以還會多產生 `src/<專案名稱>/__init__.py`（裡面有一個示範用的 `main()` 函式），`pyproject.toml` 裡也會多出 `[build-system]` 跟 `[project.scripts]` 這兩段設定
   - `src/` 底下這個範例套件跟這次的練習沒有關係，之後都是直接改根目錄的 `todo.py`，`src/` 資料夾可以留著不用管
4. 執行 `uv run todo.py` 確認能跑起來——**這一步會建立 `.venv` 資料夾、安裝好對應版本的 Python 並執行程式**，之後每次 `uv run` 都會沿用同一個環境
5. 在 **main** 分支上做第一次 commit（這次會連 `pyproject.toml`、`.python-version`、`uv.lock` 一起進版控，`.venv/` 不進）：
   - **VS Code**：Source Control 面板勾選這些變更的檔案 → 輸入 commit 訊息 "init: exercise 1 project environment"→ 打勾送出 → 送出後點同步變更把 commit 推上 GitHub
   - **終端機**：

     ```bash
     git add .
     git commit -m "init: exercise 1 project environment"
     git push
     ```
6. 建立 `feature/delete-task` 分支（先不動工，晚點做 Feature 2 時才會用到）：
   - **VS Code**：點左下角目前分支名稱（此時是 `main`）→ 選 **Create new branch...** → 輸入 `feature/delete-task` → Enter（建立後會自動切換過去）
   - **終端機**：

     ```bash
     git checkout -b feature/delete-task   # 先開好，晚點才會用到
     ```

7. 切回 `main`，再從這裡建立 `feature/add-task` 分支（接下來要開始做這一條）：
   - **VS Code**：點左下角分支名稱（此時是 `feature/delete-task`）→ 切回 **main**（在清單裡選 `main`）→ 再點一次左下角分支名稱 → **Create new branch...** → 輸入 `feature/add-task` → Enter
   - **終端機**：

     ```bash
     git checkout main
     git checkout -b feature/add-task      # 接下來要開始做這一條
     ```

   這樣兩條分支的起點會是同一個 commit，`feature/delete-task` 停在這裡不動。

8. 確認目前所在分支是 `feature/add-task`（VS Code 左下角或終端機 `git branch` 都看得到），確認無誤後才開始做 Feature 1。

## Phase 2：Feature 1 — 新增任務防重複

`todo.py` 已經在專案根目錄底下（Use this template 建立 repo、clone 下來時就一起帶過來了），目前裡面只有 `add_task`、`show_tasks`、`main` 這三個部分。

1. 切換到剛剛已經建立好的 `feature/add-task` 分支：用 VS Code 左下角分支名稱點一下選取，或終端機 `git checkout feature/add-task`
2. 修改 `todo.py`：強化 `add_task`，新增前先檢查任務名稱是否已存在，重複就不新增（並印一句提示）：

   ```python
   def add_task(name):
       if name in tasks:
           print(f"'{name}' already exists, skipping")
           return
       tasks.append(name)
   ```

3. 把 `show_tasks()` 的標題從陽春的 `=== 待辦清單 ===` 改成顯示目前共有幾項：

   ```python
   def show_tasks():
       print(f"=== To-Do List ({len(tasks)} items) ===")
       for i, t in enumerate(tasks, 1):
           print(f"{i}. {t}")
   ```

4. 在 `main()` 裡加一段呼叫，demo 一下防重複有作用（新增同一個名稱兩次，第二次會被擋下來）：

   ```python
   def main():
       add_task("Learn Git")
       add_task("Learn Git")
       show_tasks()
   ```

5. 執行 `uv run todo.py` 確認輸出正確（重複的任務有被擋下、標題有顯示項目數），接著 commit 並推上 GitHub：
   - **VS Code**：Source Control 面板勾選所有變更的檔案 → 輸入 commit 訊息 → 打勾送出 → 送出後上方會出現 **Publish Branch** 按鈕，點下去
   - **終端機**：

     ```bash
     git add .
     git commit -m "add: prevent duplicate task"
     git push -u origin feature/add-task
     ```
6. 到 GitHub 網頁，點 **Compare & pull request**，base: `main` ← compare: `feature/add-task`
7. 看 **Files changed** 讀一下 diff，確認只有 `todo.py` 被改動；寫一句 PR 說明，接著點 **Create pull request** 建立這個 PR
8. PR 建立後，點 **Merge pull request** → 再點一次 **Confirm merge** 完成合併，接著回到本機把 main 同步到最新：
   - **VS Code**：左下角點分支名稱切回 **main** → 打開 Source Control 面板，點面板上方的 **Pull** 按鈕
   - **終端機**：

     ```bash
     git checkout main
     git pull
     ```
9. 執行 `uv run python todo.py`，確認 main 分支已經正確合併 Feature 1（重複的任務有被擋下、標題有顯示項目數）
10. （可選）刪除已合併的分支，養成清理習慣：
   - **VS Code**：左側 **Branches** 清單裡找到 `feature/add-task`，右鍵點選 **Delete Branch**
   - **終端機**：`git branch -d feature/add-task`

## Phase 3：Feature 2 — 刪除任務

`feature/delete-task` 這條分支是在做 Feature 1 之前就建立好的，所以它的起點還是「舊版」`todo.py`：`add_task` 還沒有防重複邏輯，標題那行還是最原始的 `=== 待辦清單 ===`。你會在這個舊版本上開發，等一下要 merge 回 main 時，main 已經被 Feature 1 更新過了，兩邊很可能會撞出衝突（conflict）——別慌，這是版本控制裡很常見的情況，接下來會帶你一步步處理。

1. 切換到 `feature/delete-task`：
   - **VS Code**：左下角點分支名稱，從清單選 `feature/delete-task`
   - **終端機**：`git checkout feature/delete-task`

2. 在 `todo.py` 裡新增 `delete_task(index)` 函式：

   ```python
   def delete_task(index):
       tasks.pop(index - 1)
   ```

3. 也把標題那行改成顯示剩餘任務數（但用詞跟 Feature 1 不一樣）：

   ```python
   def show_tasks():
       print(f"=== To-Do List ({len(tasks)} remaining) ===")
       for i, t in enumerate(tasks, 1):
           print(f"{i}. {t}")
   ```

4. 在 `main()` 裡加一段呼叫，demo 一下 `delete_task` 有作用（刪除前後各印一次清單）：

   ```python
   def main():
       add_task("Learn Git")
       show_tasks()
       delete_task(1)
       show_tasks()
   ```

5. commit 並推上 GitHub：
   - **VS Code**：Source Control 面板勾選變更的檔案 → 輸入 commit 訊息 → 打勾送出 → 點 **Publish Branch**
   - **終端機**：

     ```bash
     git add .
     git commit -m "add: delete_task"
     git push -u origin feature/delete-task
     ```

6. 到 GitHub 網頁，點 **Compare & pull request** 開一個新 PR（base: `main` ← compare: `feature/delete-task`）
   - 這個頁面（Comparing changes）上，title 欄位會自動帶入剛剛的 commit 訊息（例如 `add: delete_task`），可以直接用或自己修改；description 欄位可留空或簡單寫一句說明
   - 注意頁面上方會出現紅字 **Can't automatically merge.**（如圖）——這是 GitHub 提前告訴你 `main` 跟 `feature/delete-task` 已經衝突了，但不影響先建立 PR，訊息旁也寫了 **Don't worry, you can still create the pull request.**
   - 確認無誤後點 **Create pull request** 建立這個 PR

7. PR 建立後，會直接進到這個 PR 的頁面，這時候就能看到衝突狀態，不用等到手動按 merge 才發現：
   - 標題旁邊會出現紅底的 **Merge conflicts** 標籤
   - 下面會有一個警告框寫 **This branch has conflicts that must be resolved**，並列出衝突的檔案（這裡是 `todo.py`），旁邊有 **Resolve conflicts** 按鈕
   - 原本的 **Merge pull request** 按鈕這時候會是灰色、按不下去的狀態，要等衝突解決後才會恢復

   衝突的原因是：兩邊都改了 `show_tasks()` 最上面那一行標題，但改成不一樣的內容。點進 **Resolve conflicts** 後，畫面上會看到類似這樣的衝突標記（下面的「main」「feature/delete-task」是用來標示這是哪一邊的版本，實際畫面上的呈現方式可能略有不同）：

   ```python
   <<<<<<< main
       print(f"=== To-Do List ({len(tasks)} items) ===")      # 這是 Feature 1 已經 merge 進 main 的版本
   =======
       print(f"=== To-Do List ({len(tasks)} remaining) ===")    # 這是你在 feature/delete-task 上寫的版本
   >>>>>>> feature/delete-task
   ```

   其他部分（`add_task` 的防重複邏輯、`delete_task`）都不會衝突，Git 會自動合併，只有標題這一行需要你自己決定怎麼處理。

8. **解決 conflict**：
   - 點 **Resolve conflicts** 右邊的下拉箭頭，選 **Edit on the web**（不要選 **Fix with Copilot**），會直接在 GitHub 網頁上打開衝突檔案的編輯畫面
   - 兩邊其實都在講同一件事（目前清單還有幾項），挑一種說法留下來就好，把衝突標記（`<<<<<<<`、`=======`、`>>>>>>>`）跟不要的那一行都刪掉，例如最後留下：

     ```python
     print(f"=== To-Do List ({len(tasks)} items) ===")
     ```

   - 畫面右上角原本紅色的 **1 conflict** 會消失，並出現綠色打勾的 **Resolved**，這時點右上角的 **Mark as resolved** 按鈕
   - 頁面會跳回 PR 畫面，出現綠色的 **Commit merge** 按鈕，點下去完成 merge

9. 點 Merge pull request → 再點一次 Confirm merge 完成合併，接著回到本機把 main 同步到最新：
   - **VS Code**：左下角點分支名稱切回 **main** → 打開 Source Control 面板，點面板上方的 **Pull** 按鈕
   - **終端機**：

     ```bash
     git checkout main
     git pull
     ```

   執行 `uv run todo.py` 確認兩個功能（新增防重複、刪除）都正常運作，標題顯示也正確

10. （可選）刪除已合併的分支，養成清理習慣：
    - **VS Code**：左側 **Branches** 清單裡找到 `feature/delete-task`，右鍵點選 **Delete Branch**
    - **終端機**：`git branch -d feature/delete-task`

## Phase 4：收尾與繳交

- 回顧整個流程：用 VS Code Git Graph（或 `git log --oneline --graph --all`）看目前的分支圖，應該能看到 Feature 1、Feature 2 各自從 main 分岔出去開發，Feature 1 先直接合併回 main；Feature 2 因為起點較舊，合併前多了一次「把最新 main 併回 feature 分支」的紀錄，才能再合併回 main——main 上總共會有 2 次 PR 合併紀錄
- conflict 的本質：不是誰對誰錯，而是兩條分支基於不同時間點的 main 各自開發，先合併的那一個決定了「新的現狀」，晚合併的一方需要對齊這個現狀——這是團隊協作時很常遇到的情況
- **繳交格式：GitHub repo 連結 + 一張 VS Code Git Graph 畫面截圖**