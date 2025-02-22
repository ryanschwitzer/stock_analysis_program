import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from bs4 import BeautifulSoup
import requests
import colorama
from colorama import Fore, Back, Style
colorama.init()

#----------------------------------------------------------------------=
#Home Screen
print(Fore.LIGHTGREEN_EX + 'Welcome to Ryans Stock Performance Analysis')
def key():
    print(Fore.WHITE + '\n-----------------------')
    print('|   Press Enter Key   |')
    print('|     To Continue     |')
    print('-----------------------\n')
    input()
key()

#----------------------------------------------------------------------

#Main 
def main():
    #Input
    while True:
        print(Fore.LIGHTGREEN_EX + '\nYou Can Either Type a Symbol or Pick Command From The List Below.')
        print(Fore.WHITE + '  CS. Compare Stocks')
        print('  S. Stock Screening')
        print('  P. Benefits of Program')
        print('  E. Common Errors')
        print('  Q. Quit\n')
        stock = input(Fore.LIGHTGREEN_EX + 'Which would you like to see data about?: ').upper().strip()
        stock_question_confirm = input(Fore.WHITE +  f'\nYou Are Requesting "{stock}", Is This Correct? (y/n): ').lower().strip()

        if stock_question_confirm == 'y':
            break

        elif stock_question_confirm == 'n':
            print("\nPlease Retry.\n")
        
        else:
            print('\nInvalid Input: Print (y/n)\n')

    #method of use
    if stock == 'CS':
        compare_gather()
    elif stock == 'S':
        stockscreen()
    elif stock == 'P':
        benefits()
    elif stock == 'E':
        errors()
    elif stock == 'Q':
        print(Fore.LIGHTGREEN_EX + '\nThanks For Using Ryans Stock Performance Analysis')
        exit()
    else:
        stockinfo(stock)
    return stock

#------------------------------------------------------------------------------------------------------------------------------------------CompareStart
#Get stock info
def get_stock_data(stock):
    try:
        stock = yf.Ticker(stock)

        ticker = stock.history(period="1d")
        if ticker.empty:
            print(f"Error: {stock} is invalid Symbol.")
            main()
            return None
        return stock
    except Exception as e:
        print(f'Unexpected Error: {e}')
        main()
        return None
    

#Get time frame
def timeframe():
    print()

    time_dict = {
        '1 Day': '1d','5 Days': '5d','1 Month': '1mo','3 Months': '3mo','6 Months': '6mo','1 Year': '1y','2 Years': '2y','5 Years': '5y','10 Years': '10y','Year to Date': 'ytd','All-Time': 'max'
}
    time_list = list(time_dict.values())
        #Get time frame
    while True:
        print(Fore.LIGHTGREEN_EX + 'Time Frame Options:')
        for key, value in time_dict.items():
            print(Fore.WHITE + f" {value}: {key}")

        time_frame = input(Fore.LIGHTGREEN_EX + '\nWhat time period would you like to compare: ').lower().strip()
        if time_frame in time_list:
            time_frame = time_frame
            return time_frame
        else:
            print('Invalid Input: Please try again')
    
        

#Gather Info to compare
def compare_gather():
    #Gather Stock Information
    #Grab Stocks
    print(Fore.LIGHTGREEN_EX + '\nWhat stocks would you like to compare? (Must Have Correct Spelling)')
    stock1 = input(Fore.WHITE + 'Stock 1: ').upper().strip()
    stock2 = input('Stock 2: ').upper().strip()

    confirm = input(f'\nYou Are Requesting "{stock1}" and "{stock2}", Is This Correct? (y/n): ')

    if confirm == 'y':
        print('--------------------------------------------')
    elif confirm == 'n':
        return compare_gather()
    else:
        print('\nInvalid Input: (y/n)')
        return compare_gather()
    
    #load stocks
    stock1_loaded = get_stock_data(stock1)
    stock2_loaded = get_stock_data(stock2)

    print(f'You are viewing {stock1} & {stock2}')

    #show stock info and move to compare
    try:
        print(Fore.LIGHTGREEN_EX + 'Company Information:')
        print(Fore.WHITE + f"{stock1} - Country: {stock1_loaded.info.get('country', 'N/A')}, Sector: {stock1_loaded.info.get('sector', 'N/A')}")
        print(f"{stock2} - Country: {stock2_loaded.info.get('country', 'N/A')}, Sector: {stock2_loaded.info.get('sector', 'N/A')}")

        compare_main(stock1, stock2, stock1_loaded, stock2_loaded)
    #error handling
    except Exception as e:
        print(f'Unexpected Error: {e}')


#comparing stocks
def compare_main(stock1, stock2, stock1_loaded, stock2_loaded):
    compare_options = ['Open', 'High', 'Low', 'Close', 'Volume']

    #Graph view selection
    while True:
        print(Fore.LIGHTGREEN_EX + '\nYou can compare the following:')

        for com in compare_options:
            print(Fore.WHITE + com)
        print('Back to main (Q)')

        select = input(Fore.LIGHTGREEN_EX + '\nChoose what to compare: ').title().strip()

        #compare graph setup
        if select in compare_options:
            time_frame = timeframe()
            compare_graph(stock1, stock1_loaded, stock2, stock2_loaded, time_frame, select)
            break
        elif select == 'Q':
            return main()
        else:
            print('Invalid Input: Please try again.')
    return select


def compare_graph(stock1, stock1_loaded, stock2, stock2_loaded, time_frame, select):
    stock1_data = stock1_loaded.history(period=time_frame)
    stock2_data = stock2_loaded.history(period=time_frame)

    #Graphing
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    #Y Axis1
    fig.add_trace(go.Scatter(
        x=stock1_data.index, 
        y=stock1_data[select], 
        mode='lines+markers', 
        name=f"{stock1} {select}", 
        marker=dict(color='red', symbol='circle')
    ), secondary_y=False)

    #Y Axis2
    fig.add_trace(go.Scatter(
        x=stock2_data.index, 
        y=stock2_data[select], 
        mode='lines+markers', 
        name=f"{stock2} {select}", 
        marker=dict(color='blue', symbol='x')
    ), secondary_y=True)

    #Custom Layout
    fig.update_layout(
        title=f"{stock1} vs {stock2} {select}",
        xaxis_title="Date",
        legend=dict(x=0, y=1),
        template="plotly_white"
    )

    #Labels
    fig.update_yaxes(title_text=f"{stock1} {select}", title_font=dict(color="red"), tickfont=dict(color="red"), secondary_y=False)
    fig.update_yaxes(title_text=f"{stock2} {select}", title_font=dict(color="blue"), tickfont=dict(color="blue"), secondary_y=True)

    # Show interactive plot
    fig.show()

    #Continue Loop
    while True:
        proceed = input(Fore.WHITE + 'Would you like to continue comparing these stocks? (y/n): ').lower().strip()      
        if proceed == 'y':
            compare_main(stock1, stock2, stock1_loaded, stock2_loaded)
            break
        elif proceed == 'n':
            main()
            break
        else:
            print('Invalid Input: Please try again.')
#------------------------------------------------------------------------------------------------------------------------------------------CompareEnd


#------------------------------------------------------------------------------------------------------------------------------------------StockScreening
def stockscreen():
    url = 'https://stockanalysis.com/stocks/screener/'
    page = requests.get(url)
    page.raise_for_status()

    # Parse the HTML content
    soup = BeautifulSoup(page.text, 'html.parser')

    table = soup.find('table')

    # Extract table headers
    headers = [header.text for header in table.find_all('th')]

    rows = []
    for row in table.find_all('tr'):
        cells = row.find_all('td')
        cells = [cell.text.strip() for cell in cells]
        rows.append(cells)
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        df = pd.DataFrame(rows, columns=headers)
        print(df)

    #click to continue
    key()
    #back to main
    main()

#------------------------------------------------------------------------------------------------------------------------------------------StockScreening

#------------------------------------------------------------------------------------------------------------------------------------------Benefits


def benefits():
    #Show Benefits  
    print(Fore.LIGHTGREEN_EX + '\nThis Program Can Help You Analyze Stocks.')

    print('You Will Press Any Key To Move To Next Section Benefit.')
    
    print('We are going to use JD: JD.com as the stock example for some of the explanations.')

    key()

    #Benefit 1
    print(Fore.WHITE + """Price Trend Analysis:
Visual Inspection (Graph): The graph of the price movement over the selected time period allows you to quickly see the trend. Is the price generally rising, falling, or fluctuating? Are there any significant peaks or valleys? This gives you a sense of the stock's recent volatility.
Numerical Analysis: The table of Open, High, Low, and Close prices for each day allows for more precise analysis. You can calculate:
Daily Change: Close Price - Open Price (Shows how much the price changed within each day).
Percentage Change: ((Close Price - Open Price) / Open Price) * 100 (Gives the daily price change as a percentage).
Range: High Price - Low Price (Measures the daily price volatility).
Trend Identification: By looking at the closing prices over the time period, you can try to identify a trend (uptrend, downtrend, or sideways movement).""")
    key()

    #Benefit 2
    print("""Volume Analysis:
Volume and Price Correlation: Compare the daily trading volume with the price movements. Generally, higher volume during price increases suggests stronger buying interest, while higher volume during price decreases may indicate stronger selling pressure. Look for divergences – sometimes a price increase with low volume can be a warning sign.
Average Volume: Calculate the average daily trading volume over the time period. This provides a baseline to compare against individual days. Unusually high or low volume can be significant.""")
    key()

    #Benefit 3
    print("""Dividend and Stock Split Information:
No Activity: In your example, the "Empty DataFrame" indicates that there were no dividends or stock splits during the selected time period. This is important information, as these events can significantly impact stock prices.""")
    
    key()

    #Benefit 4
    print("""Fundamental Analysis (Revenue):
Revenue Growth: The provided revenue data allows you to assess the company's revenue growth over the past few years. Calculate the year-over-year percentage change in revenue to see the growth trend. Is the company's revenue increasing, decreasing, or staying relatively flat?
Comparison: Compare JD.com's revenue growth with its competitors or the industry average to see how it's performing relative to others.""")
    
    key()

    #Benefit 5
    print("""Sector and Region Information:
Context: Knowing that JD.com is in the "Consumer Cyclical" sector and operates in "China" provides important context for your analysis. Consumer cyclical stocks are sensitive to economic conditions, so understanding the economic outlook for China is relevant. You can also compare JD.com's performance to other consumer cyclical companies in China or globally.""")
    
    key()

    #Benefit 6
    print("""Further Research:
The information provided by your program is a good starting point, but you should conduct further research before making any investment decisions. Consider:

Analyst Ratings: What are analysts' opinions on the stock?
News and Events: Are there any recent news or events that could impact the company's performance?
Financial Statements: Review the company's financial statements (balance sheet, income statement, cash flow statement) for a more in-depth understanding of its financial health.""")

    key()
    main()


#------------------------------------------------------------------------------------------------------------------------------------------Benefits


def errors():
    #print errors i found
    print('\n1. "Unexpected error: Too Many Requests. Rate limited. Try after a while." Complete The Command "pip install yfinance --upgrade --no-cache-dir "')
    key()
    main()


#------------------------------------------------------------------------------------------------------------------------------------------Benefits


def stockinfo(stock):
    #show stock your viewing
    stock_info = get_stock_data(stock)
    print(Fore.LIGHTGREEN_EX + f'\nYou are now viewing {stock}')

    #Show info about stock
    print(Fore.WHITE + f"Company: {stock_info.info['longName']}")
    print(f"Sector: {stock_info.info['sector']}")
    print(f"Industry: {stock_info.info['industry']}")
    print(f"Market Cap: {stock_info.info['marketCap']}")
    print(f"P/E Ratio: {stock_info.info['trailingPE']}")

    key()
    stock_main(stock, stock_info)
    return stock_info


def stock_main(stock, stock_info):
    #options to do with stock
    print(Fore.LIGHTGREEN_EX + f'\nOptions To Analyze {stock}')
    print(Fore.WHITE + '1. Stock Trade Data')
    print('2. Dividends/Stock Splits')
    print('3. Balance Sheet')
    print('4. Income Statement')
    print('5. Company Revenue')
    print('6. Back To Home\n')
    gather_info = (input(Fore.LIGHTGREEN_EX + 'What Would You Like To See?: ')).strip()

    stock_option(stock, gather_info, stock_info)
    return gather_info, stock_info


def stock_option(stock, gather_info, stock_info):
    #stock trade data
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        if gather_info == '1':
            time_frame = timeframe()
            stock_data = stock_info.history(period=time_frame)
            print(Fore.WHITE + f'{stock_data}')
            
            change = stock_data['Open'].iloc[-1] - stock_data['Open'].iloc[0]
            per_change = (change / stock_data['Open'].iloc[0]) * 100

            print(Fore.WHITE + f'\n{stock} has changed $ {change}, this is a change of {per_change} %\nThis took place from {stock_data.index[0].date()} to {stock_data.index[-1].date()}')

            #Question about graphing
            while True:
                graph = input(Fore.LIGHTGREEN_EX + f'\nWould you like to see {stock} graphed? (y/n): ').lower().strip()
                if graph == 'y':
                    idv_pregraph(stock_data, stock, stock_info)
                    break
                elif graph == 'n':
                    stock_main(stock)
                    break
                else:
                    print('Invalid Input: Please try again.')
        #Dividends/stocksplits
        elif gather_info == '2':
            print(Fore.LIGHTGREEN_EX + '\nIf there is Dividends or Stock Splits, it will print under this line:')
            try:
                print('\nDividends')
                print(Fore.WHITE + stock_info.dividends)
                print(Fore.LIGHTGREEN_EX + 'Stock Splits')
                print(Fore.WHITE + stock_info.splits)
            except Exception as e:
                print(f'Unexpected Error: {e}')
            key()
        #balance sheet
        elif gather_info == '3':
            print(Fore.LIGHTGREEN_EX + "\nBalance Sheet:")
            try:
                print(Fore.WHITE + f'{stock_info.balance_sheet}')
            except Exception as e:
                print(f'Unexpected Error: {e}')    
            key()
        #income statements
        elif gather_info == '4':
            print(Fore.LIGHTGREEN_EX + "\nIncome Statement:")
            try:
                print(Fore.WHITE + f'{stock_info.financials}')
            except Exception as e:
                print(f'Unexpected Error: {e}')
            key()
        #total revenue
        elif gather_info == '5':
            print(Fore.LIGHTGREEN_EX + '\nTotal Revenue')
            try:
                income_statement = stock_info.financials
                print(Fore.WHITE + f'{income_statement.loc["Total Revenue"]}')
            except Exception as e:
                print(f'Unexpected Error: {e}')
            key()
        #back to home
        elif gather_info == '6':
            main()
        #error handling
        else:
            print('Invalid Input: Please try again.')

        #go back to main
        stock_main(stock, stock_info)

    #saving stock data
    return stock_data


#pre graph info
def idv_pregraph(stock_data, stock, stock_info):
    #Availible options to view
    view_options = ['Open', 'High', 'Low', 'Close']

    while True:
        print(Fore.LIGHTGREEN_EX + '\nPick two data sets to graph:')

        for view in view_options:
            print(Fore.WHITE + view)
        print('Back to main (Q)')

        #Questinos about graph
        select1 = input(Fore.LIGHTGREEN_EX + '\nChoose first data set to graph: ').title().strip()
        select2 = input('\nChoose second data set to graph: ').title().strip()

        if select1 and select2 in view_options:
            idv_graph(stock_data, select1, select2, stock, stock_info)
            break
        elif select1 == 'Q':
            return main()
        else:
            print('Invalid Input: Please try again.')

    #return graph questions
    return select1, select2,


def idv_graph(stock_data, select1, select2, stock, stock_info):
    fig = go.Figure()
    # Add Open Price Line
    fig.add_trace(go.Scatter(
        x=stock_data.index, 
        y=stock_data[f'{select1}'], 
        mode='lines+markers', 
        name=f"{stock} {select1} Price", 
        marker=dict(color='red')
    ))

    # Add Close Price Line
    fig.add_trace(go.Scatter(
        x=stock_data.index, 
        y=stock_data[f'{select2}'], 
        mode='lines+markers', 
        name=f"{stock} {select2} Price", 
        marker=dict(color='blue')
    ))

    # Customize Layout
    fig.update_layout(
        title=f"{stock} Stock Price Over Time",
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        legend=dict(x=0, y=1),
        template="plotly_white"
    )

    # Show the interactive plot
    fig.show()

    stock_main(stock, stock_info)


#Call Start of Program
stock = main()