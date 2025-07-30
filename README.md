# Pytest + Playwright + Allure 自動化登入測試專案

這是一個使用 **Pytest + Playwright** 建構的 UI 自動化測試專案，針對登入功能進行正向與負向測試。  
報告部分整合 **Allure**，並支援在 Jenkins 上執行並產生可視化報告。

---

# 使用技術

- Python 3.10+
- [Playwright](https://playwright.dev/python/)
- [Pytest](https://docs.pytest.org/)
- [Allure Report](https://docs.qameta.io/allure/)
- Jenkins（整合 CI/CD）

---
# 執行測試並輸出結果到 allure-results/
pytest test_login.py --alluredir=allure-results

# 開啟 Allure 報告（需已安裝 Java 和 Allure CLI）
allure serve allure-results
或產出靜態報告：

編輯
allure generate allure-results -o allure-report --clean