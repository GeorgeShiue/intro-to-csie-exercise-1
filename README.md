# Exercise 1 實作教學

這次實作會透過一支簡單的待辦清單 CLI 程式，讓你練習 Git、GitHub 與 uv 的基本操作。

## Step 1：建立專案骨架

1. 開範例 repo：[https://github.com/GeorgeShiue/intro-to-csie-exercise-1](https://github.com/GeorgeShiue/intro-to-csie-exercise-1)，點頁面右上角綠色的 **Use this template** 按鈕 → 選 **Create a new repository**，建立自己的 repo
   - 這一步是把這個範例 repo 當「模板」，複製一份完全獨立的新 repo 到你自己的 GitHub 帳號底下（有自己的 commit 歷史，跟原本的範例 repo 沒有關聯）。這跟 fork 不同：fork 會保留與原 repo 的關聯，template 則不會，適合當作個人作業的起點
   - 依畫面指示輸入 repo 名稱、選擇 Public 或 Private，按 **Create repository**
2. 在自己電腦上，用 VS Code 的 **Source Control → Clone Repository**（或終端機 `git clone <自己 repo 的網址>`），把 repo clone 到本機資料夾
3. 用 VS Code 開啟這個資料夾，在內建終端機執行 `uv init`（可加 `--python 3.14` 指定版本），**在寫任何程式之前先把專案的環境設定準備好**
   - 這一步會產生：`pyproject.toml`（宣告這個專案用什麼 Python 版本、之後會裝什麼套件）、`.python-version`、`uv.lock`（鎖定目前這個專案還沒有任何依賴的狀態）——`.venv/` 資料夾這時候還沒被建立
4. 檢查資料夾裡有沒有 `.gitignore`；如果沒有，自己建立一個，內容至少要排除 `.venv/`、`__pycache__/` 這類環境相關檔案，避免等一下不小心把它們 commit 進版控
5. 執行 `uv run python todo.py` 確認能跑起來——**這一步才會真正建立 `.venv` 資料夾、安裝好對應版本的 Python 並執行程式**，之後每次 `uv run` 都會沿用同一個環境
6. 在 **main** 分支上做第一次 commit（這次會連 `pyproject.toml`、`.python-version`、`uv.lock` 一起進版控，`.venv/` 不進）：用 VS Code 左側 Source Control 面板操作（勾選檔案 → 輸入 commit 訊息 → 打勾送出），或終端機 `git add` / `git commit` / `git push`
7. 把 Feature 1、Feature 2 的分支都先建好，但先不動工：

   - **VS Code**：點左下角目前分支名稱（此時是 `main`）→ 選 **Create new branch...** → 輸入 `feature/delete-task` → Enter（建立後會自動切換過去）→ 再點左下角分支名稱（此時是 `feature/delete-task`）→ 切回 **main**（在清單裡選 `main`）→ 再點一次左下角分支名稱 → **Create new branch...** → 輸入 `feature/complete-task` → Enter
   - **終端機**：

     ```bash
     git checkout -b feature/delete-task   # 先開好，晚點才會用到
     git checkout main
     git checkout -b feature/complete-task # 接下來要開始做這一條
     ```

   這樣兩條分支的起點會是同一個 commit，`feature/delete-task` 先停在這裡不動，等一下做 Feature 2 時會從這裡接著做。做完之後記得確認目前所在分支是 `feature/complete-task`（VS Code 左下角或終端機 `git branch` 都看得到），這樣才能開始做 Feature 1。

## Step 2：Feature 1 — 標記完成

`todo.py` 已經在專案根目錄底下（Use this template 建立 repo、clone 下來時就一起帶過來了），目前裡面只有 `add_task`、`show_tasks`、`main` 這三個部分。

1. 切換到剛剛已經建立好的 `feature/complete-task` 分支：用 VS Code 左下角分支名稱點一下選取，或終端機 `git checkout feature/complete-task`
2. 修改 `todo.py`（**`tasks` 本身維持純字串陣列，不用改結構**，完成狀態改用另外一個獨立的集合記錄）：

   ```python
   completed = set()

   def complete_task(index):
       completed.add(index)

   def show_tasks():
       print(f"=== 待辦清單（已完成 {len(completed)}/{len(tasks)}）===")
       for i, t in enumerate(tasks, 1):
           mark = "[x]" if i in completed else "[ ]"
           print(f"{mark} {i}. {t}")
   ```

3. 用 `uv add` 加一個套件讓顯示更清楚：
   - 執行 `uv add rich`，跑完後可以看一下發生了什麼：`pyproject.toml` 多了一行依賴、`uv.lock` 被更新（鎖定 `rich` 的確切版本），`.venv/` 裡也真的裝進了這個套件
   - 把顯示 `[x]`/`[ ]` 標記那一行的 `print` 換成 `rich` 提供的彩色輸出（例如完成的任務印成綠色），一兩行程式碼即可——**上一步剛改好的標題那一行（顯示「已完成 X/Y」的那行 `print`）先不要動，這次只動 `[x]`/`[ ]` 那一行**
   - `pyproject.toml`、`uv.lock` 這兩個檔案也要一起加進這次的 commit，`.venv/` 依然不用（已經在 `.gitignore` 排除）
4. 執行 `uv run python todo.py` 確認輸出正確（顏色有出現），接著 commit 並推上 GitHub：
   - **VS Code**：Source Control 面板勾選所有變更的檔案 → 輸入 commit 訊息 → 打勾送出 → 送出後上方會出現 **Publish Branch** 按鈕，點下去
   - **終端機**：

     ```bash
     git add .
     git commit -m "add complete_task and colorize output"
     git push -u origin feature/complete-task
     ```
5. 到 GitHub 網頁，點 **Compare & pull request**，base: `main` ← compare: `feature/complete-task`
6. 看 **Files changed** 讀一下 diff——這次除了 `todo.py` 的程式碼變更，還會看到 `pyproject.toml`、`uv.lock` 也一併被記錄；寫一句 PR 說明
7. 點 **Merge pull request**，接著回到本機把 main 同步到最新：
   - **VS Code**：左下角點分支名稱切回 **main** → 點狀態列上的同步圖示（一個帶箭頭的圓形符號，會顯示要 pull 的數量）
   - **終端機**：

     ```bash
     git checkout main
     git pull
     ```
8.（可選）刪除已合併的分支，養成清理習慣：
   - **VS Code**：左側 **Branches** 清單裡找到 `feature/complete-task`，右鍵點選 **Delete Branch**
   - **終端機**：`git branch -d feature/complete-task`

## Step 3：Feature 2 — 刪除任務

`feature/delete-task` 這條分支是在做 Feature 1 之前就建立好的，所以它的起點還是「舊版」`todo.py`：沒有 `completed`、沒有 `complete_task`、還沒裝 `rich` 套件、標題那行還是最原始的 `=== 待辦清單 ===`。你會在這個舊版本上開發，等一下要 merge 回 main 時，main 已經被 Feature 1 更新過了，兩邊很可能會撞出衝突（conflict）——別慌，這是版本控制裡很常見的情況，接下來會帶你一步步處理。

1. 切換到 `feature/delete-task`：
   - **VS Code**：左下角點分支名稱，從清單選 `feature/delete-task`
   - **終端機**：`git checkout feature/delete-task`

2. 在 `todo.py` 裡新增 `delete_task(index)` 函式 → 順手把標題那行也改成顯示剩餘任務數：

   ```python
   def delete_task(index):
       tasks.pop(index - 1)

   def show_tasks():
       print(f"=== 待辦清單（共 {len(tasks)} 項）===")
       for i, t in enumerate(tasks, 1):
           print(f"{i}. {t}")
   ```

3. commit 並推上 GitHub：
   - **VS Code**：Source Control 面板勾選變更的檔案 → 輸入 commit 訊息 → 打勾送出 → 點 **Publish Branch**
   - **終端機**：

     ```bash
     git add .
     git commit -m "add delete_task"
     git push -u origin feature/delete-task
     ```

4. 到 GitHub 網頁，點 **Compare & pull request** 開一個新 PR（base: `main` ← compare: `feature/delete-task`）

5. 準備 merge 這個 PR 時，會看到衝突提示：兩邊都改了 `show_tasks()` 最上面那一行標題，但改成不一樣的內容。畫面上會看到類似這樣的衝突標記（下面的「main」「feature/delete-task」是用來標示這是哪一邊的版本，實際畫面上的呈現方式可能略有不同）：

   ```python
   <<<<<<< main
       print(f"=== 待辦清單（已完成 {len(completed)}/{len(tasks)}）===")   # 這是 Feature 1 已經 merge 進 main 的版本
   =======
       print(f"=== 待辦清單（共 {len(tasks)} 項）===")                     # 這是你在 feature/delete-task 上寫的版本
   >>>>>>> feature/delete-task
   ```

   其他部分（`complete_task`、`delete_task`、`[x]`/`[ ]` 標記那一行）都不會衝突，Git 會自動合併，只有標題這一行需要你自己決定怎麼處理。

6. **解決 conflict**：直接在 GitHub 網頁點 **Resolve conflicts** 圖形化介面處理即可。仔細看會發現 Feature 1 的版本其實已經內含 `len(tasks)`（總任務數），兩邊資訊可以合併成一行，例如：

   ```python
   print(f"=== 待辦清單（已完成 {len(completed)}/{len(tasks)} 項）===")
   ```

   確認送出，完成 merge

7. 點 **Merge pull request**，接著回到本機把 main 同步到最新：
   - **VS Code**：左下角點分支名稱切回 **main** → 點狀態列上的同步圖示（一個帶箭頭的圓形符號，會顯示要 pull 的數量）
   - **終端機**：

     ```bash
     git checkout main
     git pull
     ```

   執行 `uv run python todo.py` 確認三個功能（新增、標記完成、刪除）都正常運作，標題顯示正確，完成任務的顏色也還在（merge 之後 `rich` 相關的程式碼會一起帶進來，不需要重新安裝）

8.（可選）刪除已合併的分支，養成清理習慣：
   - **VS Code**：左側 **Branches** 清單裡找到 `feature/delete-task`，右鍵點選 **Delete Branch**
   - **終端機**：`git branch -d feature/delete-task`

## Step 4：收尾與繳交

- 回顧一下整個流程：main 上會有 2 次「功能合併」的紀錄，其中第 2 次（Feature 2）含一次 conflict 解決，可以用 `git log --oneline` 或 GitHub 的 **Insights → Network** 圖示看到分支合併的軌跡
- conflict 的本質：不是誰對誰錯，而是兩條分支基於不同時間點的 main 各自開發，先合併的那一個決定了「新的現狀」，晚合併的一方需要對齊這個現狀——這是團隊協作時很常遇到的情況
- 繳交格式：GitHub repo 連結 + 一張 VS Code Git Graph 畫面截圖：走完 Feature 1、2（含 conflict 解決）後，能看到 main 分支上 2 次合併紀錄的分支圖
