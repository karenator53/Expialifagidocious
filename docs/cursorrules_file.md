# Updated Cursor Rules for Project

## Project Overview

**Project Name:** Real-Time Wallet Tracker

**Description:** Develop a real-time wallet tracking application that monitors wallets on the Sonic, Base, and Solana blockchains. The application integrates with Sonic Labs and Sonicscan APIs and provides real-time tracking of wallet balances and transactions, profit and loss calculations, monitoring of remaining coin balances, and real-time detection of trades for possible copy trading. Users can input multiple wallet addresses, organizing them into groups or categories for tailored tracking. The application is accessed with a single shared account, simplifying entry.

**Tech Stack:**

*   Frontend: React.js
*   Backend: Python with FastAPI
*   Database: MongoDB
*   APIs: Sonic Labs, Sonicscan
*   Development Tools: Bolt, Claude AI, ChatGPT, Cursor AI IDE
*   Deployment: Docker

**Key Features:**

*   Real-time wallet tracking
*   Profit and Loss (PnL) calculations
*   Monitoring remaining coin balances
*   Trade detection for the purposes of copy trading
*   Grouping and categorizing wallets for tailored tracking

## Project Structure

**Root Directory:**

*   Contains the main configuration files and documentation such as README.md, Dockerfile, docker-compose.yml, and environment settings.

**/frontend:**

*   Contains all frontend-related code, including components, styles, and assets. **/components:**

    *   WalletTracker
    *   PnLCalculator
    *   TradeDetector

*   **/assets:**

    *   Logo.svg
    *   Icons/

*   **/styles:**

    *   variables.scss
    *   WalletTracker.module.css

**/backend:**

*   Contains all backend-related code, including API routes and database models implemented in FastAPI. **/controllers:**

    *   walletController.py
    *   transactionController.py

*   **/models:**

    *   walletModel.py
    *   transactionModel.py

*   **/routes:**

    *   walletRoutes.py
    *   transactionRoutes.py

**/config:**

*   Configuration files for environment variables and application settings.

    *   databaseConfig.py
    *   apiConfig.py

**/tests:**

*   Contains unit and integration tests for both frontend and backend.

## Development Guidelines

**Coding Standards:**

*   Follow PEP 8 for Python and Airbnb JavaScript style guide for JavaScript. Utilize Flake8 for Python linting and ESLint for JavaScript.

**Component Organization:**

*   Organize React components in a modular fashion, each within its own folder containing corresponding styles and tests.

## Cursor IDE Integration

**Setup Instructions:**

1.  Clone the repository.
2.  Run `npm install` in the `/frontend` directory.
3.  Run `pip install -r requirements.txt` in the `/backend` directory.
4.  Set up environment variables in `/config`.

**Deployment Instructions:**

1.  Ensure Docker is installed and running.
2.  Use `docker-compose up` to build and run the application containerized environment.

**Key Commands:**

*   `npm run dev`: Starts the frontend development server.
*   `uvicorn backend.main:app --reload`: Starts the FastAPI backend server.
*   `docker-compose up`: Deploys the application in Docker containers.
*   `npm test` and `pytest`: Run tests for frontend and backend, respectively.

## Additional Context

**User Interface:**

*   Upon login, a list view of wallets is displayed, showing balances and key metrics.
*   Focus on clean, accessible UI with ARIA tags as needed. Use color coding for PnL visualization.

**Performance Considerations:**

*   Implement efficient API usage with a focus on minimizing calls while maintaining real-time updates.

**User Base:**

*   Designed for individual investors as a tool, not requiring specific user roles or extensive onboarding.

This document outlines the comprehensive structure and guidelines for developing the Real-Time Wallet Tracker application, incorporating Python FastAPI backend transitions and Docker deployment strategies.
