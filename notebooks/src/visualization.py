import plotly.graph_objs as go

def plot_stock_trends(data):
    fig = go.Figure()
    for company in data.columns[1:]:
        fig.add_trace(go.Scatter(x=data['Date'], y=data[company],
                                 mode='lines',
                                 name=company,
                                 opacity=0.5))
    fig.update_layout(
        title='Stock Price Trends of All Indian Companies',
        xaxis_title='Date',
        yaxis_title='Closing Price (INR)',
        xaxis=dict(tickangle=45),
        legend=dict(x=1.05, y=1, traceorder="normal", font=dict(size=10), orientation="v"),
        margin=dict(l=0, r=0, t=30, b=0),
        hovermode='x',
        template='plotly_white'
    )
    return fig

def plot_expected_investment_value(years, future_values):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=[str(year) + " year" for year in years],
        y=future_values,
        mode='lines+markers',
        line=dict(color='blue'),
        marker=dict(size=8),
        name='Future Value'
    ))
    fig.update_layout(
        title="Expected Value of Investments of ₹ 5000 Per Month (Mutual Funds)",
        xaxis_title="Investment Period",
        yaxis_title="Future Value (INR)",
        xaxis=dict(showgrid=True, gridcolor='lightgrey'),
        yaxis=dict(showgrid=True, gridcolor='lightgrey'),
        template="plotly_white",
        hovermode='x'
    )
    return fig

def plot_roi_comparison(expected_roi_mutual_fund, expected_roi_growth_companies):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=expected_roi_mutual_fund.index,
        x=expected_roi_mutual_fund,
        orientation='h',
        name='Mutual Fund Companies',
        marker=dict(color='blue')
    ))
    fig.add_trace(go.Bar(
        y=expected_roi_growth_companies.index,
        x=expected_roi_growth_companies,
        orientation='h',
        name='Growth Rate Companies',
        marker=dict(color='green'),
        opacity=0.7
    ))
    fig.update_layout(
        title='Expected ROI Comparison: Mutual Fund vs Growth Rate Companies',
        xaxis_title='Expected ROI (%)',
        yaxis_title='Companies',
        barmode='overlay',
        legend=dict(title='Company Type'),
        template='plotly_white'
    )
    return fig
