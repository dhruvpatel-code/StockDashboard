# Stock Dashboard

This is an advanced stock dashboard web application built using Dash, a Python framework for building analytical web applications. The dashboard fetches stock market data using the Yahoo Finance API and visualizes it with interactive charts. The application uses caching for performance enhancement and efficient data retrieval. Here are the key features and components of the application:

- **Stock Ticker Input**: Users can enter the ticker symbol of the desired stock to display the corresponding data. The input field supports autocomplete functionality for ease of use.

- **Date Range Selector**: Users can select a specific date range for which they want to view the stock data. The date range is presented using a DatePickerRange component.

- **Line Chart**: The line chart displays the closing prices, volume, Simple Moving Average (SMA), and Relative Strength Index (RSI) of the selected stock over time. 

- **Candlestick Chart**: The candlestick chart represents the open, high, low, and close prices of the selected stock, providing a more detailed view of price movements.

- **Data Caching**: The application utilizes Flask-Caching to cache the fetched stock data, reducing the number of API calls and improving performance.

## How to Run

To run the Stock Dashboard application, follow these steps:

1. Install the necessary dependencies by running the following command:
   ```
   pip install dash dash-core-components dash-html-components dash-bootstrap-components pandas yfinance plotly flask_caching ta
   ```

2. Clone the repository or download the source code.

3. Run the Python application using the command:
   ```
   python app.py
   ```

4. Open a web browser and navigate to `http://localhost:8050` to access the Stock Dashboard.

## Usage

1. Enter the ticker symbol of the desired stock in the stock ticker input field.

2. Select the desired date range using the date picker.

3. The line chart and candlestick chart will update to display the relevant data for the selected stock over the chosen date range.

## Future Improvements

Here are some potential improvements and additional features that can be added to the Stock Dashboard:

- More financial indicators such as Moving Average Convergence Divergence (MACD), Bollinger Bands, etc.
- Ability for users to select different chart types (e.g., bar chart, area chart) for visualizing the stock data.
- Enhancements to interactivity, such as hover-over tooltips to display precise values on the charts.
- Integration of news feeds to display relevant news articles related to the selected stock.
- Support for additional asset classes like bonds, commodities, cryptocurrencies, forex, etc.
- Comparison feature to enable users to compare multiple stocks on the same chart.
- Improve visual aesthetics by adding themes, color schemes, and responsive design for mobile devices.
- Ability to download the generated charts as images or export the data as CSV files.

Feel free to experiment and build upon this codebase to create a more comprehensive and feature-rich stock dashboard application.

