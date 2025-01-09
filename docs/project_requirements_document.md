### Project Requirements Document (PRD)

1.  Project Overview The goal is to develop a real-time wallet tracking application specifically designed for individual investors. This application will allow users to monitor cryptocurrency wallets on the Sonic, Base, and Solana blockchains. Key features include real-time wallet balance tracking, insightful Profit and Loss (PnL) calculations, monitoring of coin trades, and detecting trading activities for copy trading purposes. Integration with Sonic Labs and Sonicscan APIs will facilitate data acquisition. Primary objectives for the application include delivering precise real-time data, ensuring robust performance with rapid response, and maintaining a clean, user-friendly interface. The application will serve as a cost-effective tool for individual investors to gain insights into their crypto investments without extensive API use.

2.  In-Scope vs. Out-of-Scope **In-Scope:**

    *   Real-time tracking of wallet balances and transactions
    *   PnL calculations with numeric and color-coded indicators
    *   Trade detection for copy trading
    *   User-friendly interface
    *   Grouping of wallets for personalized tracking
    *   Integration with Sonic Labs and Sonicscan APIs

3.  **Out-of-Scope:**

    *   User roles or personalized permissions
    *   Monetization strategies
    *   Support for additional blockchains beyond Sonic, Base, and Solana
    *   Advanced security measures beyond basic data protection

4.  User Flow Users will access the application using a single shared account, since onboarding is unnecessary. Upon entering, users will see a comprehensive list view of all tracked wallets, with options to filter or categorize them for tailored tracking. Real-time updates will provide details on wallet balances, transaction history, and trades.

5.  Core Features

    *   **Real-Time Wallet Tracking:** Continuous updates from Sonic, Base, and Solana blockchains
    *   **Profit and Loss (PnL) Calculations:** Display in numeric form with green/red indicators
    *   **Trade Detection for Copy Trading:** Monitor trade activities on blockchains
    *   **APIs Integration:** Interface with Sonic Labs and Sonicscan for accurate data
    *   **Clean User Interface:** Prioritize usability and quick access
    *   **Grouping of Wallets:** Enhance tracking by organizing wallets

6.  Tech Stack & Tools

    *   **Frontend:** Frameworks like React.js considered but not confirmed
    *   **Backend:** Python with FastAPI
    *   **Database:** MongoDB
    *   **APIs:** Integration with Sonic Labs and Sonicscan
    *   **Development Tools:** Bolt, Claude AI, ChatGPT, Cursor AI
    *   **Deployment:** Utilize Docker for deployment

7.  Non-Functional Requirements

    *   **Performance:** Quick response times for real-time updates
    *   **Usability:** Intuitive interface that supports user workflow
    *   **Compliance:** Basic data protection compliance

8.  Constraints & Assumptions

    *   Success relies on the stable operation of Sonic Labs and Sonicscan APIs
    *   Efficient management of API call quotas is crucial
    *   Single shared user account mitigates complexity of multiple account management

9.  Known Issues & Potential Pitfalls

    *   **API Rate Limits:** Efficient call and caching strategies needed
    *   **Data Consistency:** Ensure integrity in real-time updates
    *   **Cross-Platform Functionality:** Consider adding multiple platforms if needed

This document aims to serve as a comprehensive guide for developing the wallet tracking application, ensuring clarity and focus throughout the project lifecycle.
