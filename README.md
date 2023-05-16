# Stock Dashboard

This program is a stock dashboard built using Python and the Dash framework. It allows you to visualize the closing prices and trading volume of selected stocks over time. You can use this program to analyze and compare the performance of different stocks.

## Installation

To use this program, you need to have Python installed on your machine. You can download Python from the official website: [python.org](https://www.python.org/).

Additionally, you need to install the required dependencies. Open a terminal or command prompt and run the following command:

```
pip install dash dash_core_components dash_html_components dash_bootstrap_components pandas yfinance plotly
```

## Usage

1. Clone or download the repository from GitHub.
2. Navigate to the project directory.
3. Run the following command to start the stock dashboard:

   ```
   python <filename>.py
   ```

   Replace `<filename>` with the name of the file containing the code.

4. Open a web browser and go to [http://localhost:8050](http://localhost:8050) to access the dashboard.

## Features

- **Stock Selection:** The dashboard provides a dropdown menu where you can select the stocks you want to analyze. By default, Apple (AAPL) is selected, but you can choose multiple stocks from the available options, including Apple, Amazon (AMZN), and Microsoft (MSFT).

- **Closing Prices:** The dashboard displays a line chart showing the closing prices of the selected stocks over time. Each stock is represented by a separate line on the chart.

- **Trading Volume:** The dashboard also includes a line chart showing the trading volume of the selected stocks over time. The volume is represented by another set of lines on the chart.

- **Date Range Selector:** You can use the date range selector on the x-axis of the chart to zoom in or out and focus on specific time periods. The available options include 1 month, 6 months, and the entire available range.

## Customization

You can customize the program to add more stocks or change the date range by modifying the code. The available stocks and their corresponding symbols are defined in the `options` list in the `dcc.Dropdown` component. You can add or remove stocks from this list as needed.

The date range for fetching stock data is set using the `start` and `end` parameters in the `yf.download` function. You can adjust these values to fetch data for a different time period.

## Contributing

If you want to contribute to this project, feel free to fork the repository and submit a pull request with your changes.

## License

This project is licensed under the [MIT License](LICENSE).
