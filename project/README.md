# Stock Portfolio Optimization

## Problem Statement

A major challenge in stock portfolio management is striking the right balance between risk and return. Risk and volatility make it difficult to determine the optimal capital allocation distribution across a stock portfolio. The goal of this project is to build a model that optimizes capital allocation across a user's stock portfolio by maximizing risk-adjusted returns using historical market data.

## Stakeholders & Users

The stakeholders for this project will be portfolio managers and individual investors

## Useful Answer & Decision

The system will use historical stock price data to calculate expected return and volatility, taking into account both expected return and risk. The user will provide a stock portfolio and the system will output an optimal percent distribution of capital across the portfolio. This system will be predictive and descriptive, predicting future stock behavior and providing metrics such as expected return, volatility, and percent allocation distribution across a portfolio.  

## Assumptions

- Stakeholders know which stocks they want to be in their portfolio
- Historical market data is useful and sufficient for predicting future stock behavior

## Possible Constraints

- Amount of available historical data
- Availability of data on certain stocks 
- Time constraints

## Possible Risks

- Insufficient computational resources for large portfolios
- The model may provide a suboptimal output due to innacurate estimation of metrics such as expected return, volatility, and risk

## Lifecycle Mapping

Define project scope and objective -> Problem Framing & Scoping (Stage 01) -> Description of project, stakeholders, assumptions, constraints, risks

## Repo Plan
/data/, /src/, /notebooks/, /docs/ ; cadence for updates

## Source

- yfinance API stock price data

## Paramrters

- Tickers: AAPL, GOOG, AMZN, MSFT, TSLA
- Date Range: 2020-08-17 - 2025-08-17, daily frequency
- Format: CSV
