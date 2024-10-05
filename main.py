from src import data_processing, analysis, visualization

data = data_processing.load_data('data/nifty50_closing_prices.csv')
roi = data_processing.calculate_roi(data)
volatility = data_processing.calculate_volatility(data)

selected_companies = analysis.select_companies(roi, volatility, roi.median(), volatility.median())
investment_ratios = analysis.calculate_investment_ratios(volatility[selected_companies.index])

stock_trends_plot = visualization.plot_stock_trends(data)
roi_comparison_plot = visualization.plot_roi_comparison(roi[selected_companies.index], roi.sort_values(ascending=False).head(10))

stock_trends_plot.show()
roi_comparison_plot.show()
print(investment_ratios.sort_values(ascending=False))