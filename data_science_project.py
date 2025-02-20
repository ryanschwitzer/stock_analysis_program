import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import msvcrt

#----------------------------------------------------------------------

#Home Screen
print('Welcome to Ryans Stock Performance Analysis')
def key():
    print('\n-----------------------')
    print('|    Press any key    |')
    print('|     To Continue     |')
    print('-----------------------\n\n')
    msvcrt.getch()
key()

#----------------------------------------------------------------------

#Repeating Terminal Loop
while True:
    def main():
        #Input
        print('\nYou Can Either Type a Nasdaq Code or Pick Command From The List Below.')
        print('CS. Compare Stocks')
        print('S. Stock Screening')
        print('P. Learn What This Program Do For You')
        print('E. Common Errors')
        print('Q. Quit\n')
        stock_question = input('Which Stock Would You Like To See Data About?: ').upper()
        stock_question_confirm = input(f'\nYou Are Requesting "{stock_question}", Is This Correct? (y/n): ')

        if stock_question_confirm == 'y':
            return stock_question

        elif stock_question_confirm == 'n':
            return main()
        
        else:
            print('Error')
            print(stock_question_confirm)
    stock_question = main()

#----------------------------------------------------------------------

#Quit | 'Q'
    if stock_question == 'Q':
        print('\nThank you for using Ryans Stock Performance Analysis')
        break

#Show 25 Stocks with Nasdaq
    elif stock_question == 'S':
        def manystock():
            companies = [
                "1. A: Agilent Technologies, Inc.",
                "2. AA: Alcoa Corporation",
                "3. AAL: American Airlines Group Inc.",
                "4. AAPL: Apple Inc.",
                "5. ABC: AmerisourceBergen Corporation",
                "6. ABMD: Abiomed, Inc.",
                "7. ABT: Abbott Laboratories",
                "8. ACGL: Arch Capital Group Ltd.",
                "9. ADBE: Adobe Inc.",
                "10. ADI: Analog Devices, Inc.",
                "11. ADP: Automatic Data Processing, Inc.",
                "12. ADSK: Autodesk, Inc.",
                "13. AEE: Ameren Corporation",
                "14. AFL: Aflac Incorporated",
                "15. AGNC: AGNC Investment Corp.",
                "16. AIG: American International Group, Inc.",
                "17. AIZ: Assurant, Inc.",
                "18. AJG: Arthur J. Gallagher & Co.",
                "19. ALB: Albemarle Corporation",
                "20. ALGN: Align Technology, Inc.",
                "21. ALLE: Allegion PLC",
                "22. ALL: Allstate Corporation",
                "23. ALXN: Alexion Pharmaceuticals, Inc.",  # Note: This was acquired by AZN
                "24. AMAT: Applied Materials, Inc.",
                "25. AMGN: Amgen Inc.",
                "26. AMP: TE Connectivity Ltd.",
                "27. AMT: American Tower Corporation",
                "28. AMZN: Amazon.com, Inc.",
                "29. ANET: Arista Networks, Inc.",
                "30. ANSS: ANSYS, Inc.",
                "31. ANTM: Anthem, Inc.", # Changed name to Elevance Health (ELV)
                "32. AON: Aon plc",
                "33. APA: APA Corporation",
                "34. APD: Air Products and Chemicals, Inc.",
                "35. APH: Amphenol Corporation",
                "36. APTV: Aptiv PLC",
                "37. ARE: Alexandria Real Estate Equities, Inc.",
                "38. ARWR: Arrowhead Pharmaceuticals, Inc.",
                "39. ASH: Ashland Global Holdings Inc.",
                "40. ATVI: Activision Blizzard, Inc.", # Acquired by Microsoft
                "41. AVB: AvalonBay Communities, Inc.",
                "42. AVGO: Broadcom Inc.",
                "43. AVY: Avery Dennison Corporation",
                "44. AXON: Axon Enterprise, Inc.",
                "45. AZN: AstraZeneca PLC",
                "46. B: Barnes Group Inc.",
                "47. BA: Boeing Company",
                "48. BAC: Bank of America Corporation",
                "49. BAX: Baxter International Inc.",
                "50. BBY: Best Buy Co., Inc.",
                "51. BDX: Becton, Dickinson and Company",
                "52. BF.B: Brown & Brown, Inc.",
                "53. BIIB: Biogen Inc.",
                "54. BKNG: Booking Holdings Inc.",
                "55. BKR: Baker Hughes Company",
                "56. BLK: BlackRock, Inc.",
                "57. BMY: Bristol Myers Squibb Company",
                "58. BR: Broadridge Financial Solutions, Inc.",
                "59. BRK.B: Berkshire Hathaway Inc. Class B",
                "60. BSX: Boston Scientific Corporation",
                "61. C: Citigroup Inc.",
                "62. CAG: Conagra Brands, Inc.",
                "63. CAH: Cardinal Health, Inc.",
                "64. CARR: Carrier Global Corporation",
                "65. CAT: Caterpillar Inc.",
                "66. CB: Chubb Limited",
                "67. CCI: Crown Castle International Corp.",
                "68. CDNS: Cadence Design Systems, Inc.",
                "69. CDW: CDW Corporation",
                "70. CE: Celanese Corporation",
                "71. CERN: Cerner Corporation",  # Acquired by Oracle
                "72. CF: CF Industries Holdings, Inc.",
                "73. CHRW: C.H. Robinson Worldwide, Inc.",
                "74. CHTR: Charter Communications, Inc.",
                "75. CI: Cigna Corporation", # Changed name to The Cigna Group (CI)
                "76. CL: Colgate-Palmolive Company",
                "77. CLX: Clorox Company",
                "78. CMCSA: Comcast Corporation",
                "79. CME: CME Group Inc.",
                "80. COG: CoreLogic, Inc.",  # Acquired by Stone Point Capital
                "81. COO: CooperCompanies, Inc.",
                "82. COP: ConocoPhillips",
                "83. COST: Costco Wholesale Corporation",
                "84. CPB: Campbell Soup Company",
                "85. CRM: Salesforce, Inc.",
                "86. CSCO: Cisco Systems, Inc.",
                "87. CSX: CSX Corporation",
                "88. CTAS: Cintas Corporation",
                "89. CTLT: Catalent, Inc.",
                "90. CTSH: Cognizant Technology Solutions Corporation",
                "91. CVX: Chevron Corporation",
                "92. D: Dominion Energy, Inc.",
                "93. DD: DuPont de Nemours, Inc.",
                "94. DDOG: Datadog, Inc.",
                "95. DE: Deere & Company",
                "96. DFS: Discover Financial Services",
                "97. DG: Dollar General Corporation",
                "98. DHR: Danaher Corporation",
                "99. DIS: The Walt Disney Company",
                "100. DLTR: Dollar Tree, Inc."
            ]

            company_string = "\n".join(companies[:25])

            print(f'\n{company_string}\n')

            more = input('Type (M) For More Stocks, Anything Else To Proceed: ').lower()

            #more
            if more == 'm':
                company_string1 = "\n".join(companies[26:50])
                print(company_string1)

                more1 = input('Type (M) For More Stocks, Anything Else To Proceed: ').lower()

                if more1 == 'm':
                    company_string2 = "\n".join(companies[51:75])
                    print(company_string2)

                    more2 = input('Type (M) For More Stocks, Anything Else To Proceed: ').lower()

                    if more2 == 'm':
                        company_string3 = "\n".join(companies[76:100])
                        print(company_string3)
                        print('\nIf You Have Not Found A Stock, Check Out: https://www.nasdaq.com/market-activity/stocks/screener?page=1&rows_per_page=25')       

                    else:
                        print("We Are Glad You Found A Stock To Analyze.")

                else:
                    print("We Are Glad You Found A Stock To Analyze.")

            else:
                print("We Are Glad You Found A Stock To Analyze.")

            print('If You Found A Stock: Type the Nasdaq Code In Terminal To See Data (Code on Left of Company Name).')

            #Call Press Key To Continue
            key()
        manystock()

    elif stock_question == 'E':
        print('\n1. "Unexpected error: Too Many Requests. Rate limited. Try after a while." Complete The Command "pip install yfinance --upgrade --no-cache-dir "')

    elif stock_question == 'P':
        def benefits():
            print('\nThis Program Can Help You Analyze Stocks.')

            print('You Will Press Any Key To Move To Next Section Benefit.')
            
            print('We are going to use JD: JD.com as the stock example for some of the explanations.')

            key()

            #Benefit 1
            print("""Price Trend Analysis:
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
        benefits()

    #Compare Stocks
    elif stock_question == 'CS':
        print('\nCOMPARE STOCKS')

        def compare():
            #Grab Stocks
            print('What stocks would you like to compare? (Must Have Correct Spelling)')
            stock1 = input('Stock 1: ').upper()
            stock2 = input('Stock 2: ').upper()

            stock_question_confirm = input(f'\nYou Are Requesting "{stock1}" and "{stock2}", Is This Correct? (y/n): ')

            def morecompare():
                if stock_question_confirm == 'y':
                    stock1_loaded = yf.Ticker(stock1)
                    stock2_loaded = yf.Ticker(stock2)
                    print()

                    #Showing Stocks
                    print(stock1_loaded)
                    print(stock2_loaded)

                    #Data Handling
                    try:
                        #printing info about company
                        country1 = stock1_loaded.info['country']
                        sector1 = stock1_loaded.info['sector']
                        country2 = stock2_loaded.info['country']
                        sector2 = stock2_loaded.info['sector']
                        print('\nSimple Company Information:')
                        print(f'\n{stock1}')
                        print(sector1)
                        print(country1)
                        print(f'\n{stock2}')
                        print(sector2)
                        print(country2)
                        
                        options1 = ['Open', 'High', 'Low', 'Close', 'Volume']

                        def compare_main():
                            def compare_input():
                                print()
                                #What is being compared
                                for op in options1:
                                    print(op)
                                print('Back To Main (Q)')
                                task = input('Choose what you want to compare from the list above: ').title()
                                return task
                            comparing_task = compare_input()
                            
                            #Compare All But Revenue
                            if comparing_task in options1:

                                #Grab Timeframe
                                print('\n1d: 1 Day\n5d: 5 Days\n1mo: 1 Month\n3mo: 3 Months\n6mo: 6 Months\n1y: 1 Year\n2y: 2 Years\n5y: 5 Years\n10y: 10 Years\nytd: Year To Date\nmax: All Time\n')
                                time_frame = input("What Time Frame Would You Like To Analyze?: ")

                                #Grabbing Data
                                stock1_data = stock1_loaded.history(period=time_frame)
                                stock2_data = stock2_loaded.history(period=time_frame)


                                #Graphing
                                fig = make_subplots(specs=[[{"secondary_y": True}]])

                                #Y Axis1
                                fig.add_trace(go.Scatter(
                                    x=stock1_data.index, 
                                    y=stock1_data[comparing_task], 
                                    mode='lines+markers', 
                                    name=f"{stock1} {comparing_task}", 
                                    marker=dict(color='red', symbol='circle')
                                ), secondary_y=False)

                                #Y Axis2
                                fig.add_trace(go.Scatter(
                                    x=stock2_data.index, 
                                    y=stock2_data[comparing_task], 
                                    mode='lines+markers', 
                                    name=f"{stock2} {comparing_task}", 
                                    marker=dict(color='blue', symbol='x')
                                ), secondary_y=True)

                                #Custom Layout
                                fig.update_layout(
                                    title=f"{stock1} vs {stock2} {comparing_task}",
                                    xaxis_title="Date",
                                    legend=dict(x=0, y=1),
                                    template="plotly_white"
                                )

                                #Labels
                                fig.update_yaxes(title_text=f"{stock1} {comparing_task}", title_font=dict(color="red"), tickfont=dict(color="red"), secondary_y=False)
                                fig.update_yaxes(title_text=f"{stock2} {comparing_task}", title_font=dict(color="blue"), tickfont=dict(color="blue"), secondary_y=True)

                                # Show interactive plot
                                fig.show()

                                #Continue
                                def keep_compare():
                                    more = input('\nWould You Like To Continue Comparing These Two Stocks? (y/n): ').lower()

                                    if more == 'y':
                                        return morecompare()
                                    
                                    elif more == 'n':
                                        main()

                                    else:
                                        print('Invalid Input')
                                        return keep_compare()
                                keep_compare()

                            elif comparing_task == 'Q':
                                main()

                            else:
                                print('\nInvalid Input')
                                return compare_main()
                        compare_main()

                    #Error Handling
                    except Exception as e:
                        print()
                        print(f'\nUnexpected error: {e}\n')
                        return morecompare()

                elif stock_question_confirm == 'n':
                    print()
                    return compare()

                else:
                    print('Invalid Input')
                    return compare()
            morecompare()
        compare()

#Custom/Error Handling
    else:
        print(f'\nYou Are Now Viewing {stock_question}\n')

        #Complete Custom Analysis
        def custom():
            try:
                with pd.option_context('display.max_rows', None, 'display.max_columns', None):
                    #Getting Stock Info
                    custom = stock_question
                    stock = yf.Ticker(custom)
                    print(stock)
                    #printing info about company
                    country = stock.info['country']
                    sector = stock.info['sector']
                    print()
                    print(sector)
                    print(country)

                    #Gathering Print Info
                    def print_info():
                        #Options
                        print(f'\nOptions To Analyze {custom}')
                        print('1. Stock Trade Data')
                        print('2. Dividends/Stock Splits')
                        print('3. Balance Sheet')
                        print('4. Income Statement')
                        print('5. Company Revenue')
                        print('6. Back To Home\n')
                        gather_info = int(input('What Would You Like To See?: '))

                        #stock trade data
                        if gather_info == 1:
                            #Gather Time Frame
    
                            print('\nYour List of Time Frames')
                            print('1d: 1 Day\n5d: 5 Days\n1mo: 1 Month\n3mo: 3 Months\n6mo: 6 Months\n1y: 1 Year\n2y: 2 Years\n5y: 5 Years\n10y: 10 Years\nytd: Year To Date\nmax: All Time\n')
                            time_frame = input("What Time Frame Would You Like To Analyze?: ").lower()

                            #Load Stock Data
                            stock_data = stock.history(period=time_frame)
                            print(stock_data)

                            #Graph
                            graph_question = input('\nWould You Like to See This Stock Price Graphed? (y/n): ')

                            if graph_question == 'y':
                                fig = go.Figure()

                                # Add Open Price Line
                                fig.add_trace(go.Scatter(
                                    x=stock_data.index, 
                                    y=stock_data['Open'], 
                                    mode='lines+markers', 
                                    name=f"{custom} Opening Price", 
                                    marker=dict(color='red')
                                ))

                                # Add Close Price Line
                                fig.add_trace(go.Scatter(
                                    x=stock_data.index, 
                                    y=stock_data['Close'], 
                                    mode='lines+markers', 
                                    name=f"{custom} Closing Price", 
                                    marker=dict(color='blue')
                                ))

                                # Customize Layout
                                fig.update_layout(
                                    title=f"{custom} Stock Price Over Time",
                                    xaxis_title="Date",
                                    yaxis_title="Price (USD)",
                                    legend=dict(x=0, y=1),
                                    template="plotly_white"
                                )

                                # Show the interactive plot
                                fig.show()
                                return print_info()
                            
                            elif graph_question == 'n':
                                return print_info()

                        #Dividends/Stock Splits
                        elif gather_info == 2:
                            print('\nIf there is Dividends or Stock Splits, it will print under this line:')
                            print(stock.actions)
                            return print_info()
                        
                        #Balance Sheets
                        elif gather_info == 3:
                            balance_sheet = stock.balance_sheet
                            print("\nBalance Sheet:")
                            print(balance_sheet)
                            return print_info()
                        
                        #Income Statements
                        elif gather_info == 4:
                            income_statement = stock.financials
                            print("\nIncome Statement:")
                            print(income_statement)
                            return print_info()

                        #Revenue
                        elif gather_info == 5:
                            def revenueinfo():
                                print('\nTotal Revenue')
                                income_statement = stock.financials
                                revenue = income_statement.loc["Total Revenue"]
                                print(revenue)

                                graph_revenue = input('\nWould You Like This Graphed? (y/n): ')

                                if graph_revenue == 'y':
                                    #Graph
                                    fig = go.Figure()

                                    # Add Total Revenue Data
                                    fig.add_trace(go.Scatter(
                                        x=income_statement.columns,  # Assuming columns represent dates
                                        y=income_statement.loc["Total Revenue"], 
                                        mode='lines+markers', 
                                        name=f"{custom} Revenue", 
                                        marker=dict(color='red', symbol='circle')
                                    ))

                                    # Customize Layout
                                    fig.update_layout(
                                        title=f"{custom} Revenue Over Time",
                                        xaxis_title="Date",
                                        yaxis_title="Revenue (USD)",
                                        legend=dict(x=0, y=1),
                                        template="plotly_white"
                                    )

                                    # Show interactive plot
                                    fig.show()
                                    return print_info()

                                elif graph_revenue == 'n':
                                    print()
                                    return print_info()
                                
                                else:
                                    print('Invalid Input')
                                    return revenueinfo()
                            revenueinfo()

                        #Goto main()
                        elif gather_info == 6:
                            main()

                        #error handling
                        else:
                            print('Invalid Input')
                            return print_info()
                        
                    print_info()

            #Error Handling
            except Exception as e:
                print(f'\nUnexpected error: {e}')
        custom()