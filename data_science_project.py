import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import msvcrt

#----------------------------------------------------------------------

#Home Screen
print('Welcome to Ryans Stock Performance Analysis')
def key():
    print()
    print('-----------------------')
    print('|    Press any key    |')
    print('|     To Continue     |')
    print('-----------------------')
    print()
    msvcrt.getch()
    print()
key()

#----------------------------------------------------------------------

#Repeating Terminal Loop
while True:
    def main():
        #Input
        print()
        print('You Can Either Type a Nasdaq Code or Pick Command From The List Below.')
        print('Compare Stocks (CS)')
        print('List Of 25 Highly Searched Stocks (S)')
        print('Learn What This Program Do For You (P)')
        print('Quit (Q)')
        print()
        stock_question = input('Which Stock Would You Like To See Data About?: ').upper()
        print()
        stock_question_confirm = input(f'You Are Requesting "{stock_question}", Is This Correct? (y/n): ')

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
        print()
        print('Thank you for using Ryans Stock Performance Analysis')
        break

#Show 25 Stocks with Nasdaq
    elif stock_question == 'S':
        def manystock():
            print()
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

            print(company_string)

            print()

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
                        print()
                        print('If You Have Not Found A Stock, Check Out: https://www.nasdaq.com/market-activity/stocks/screener?page=1&rows_per_page=25')       

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

    elif stock_question == 'P':
        def benefits():
            print()
            print('This Program Can Help You Analyze Stocks.')

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

    elif stock_question == 'CS':
        print()
        print('COMPARE STOCKS')

        def compare():

            #Grab Stocks
            print('What stocks would you like to compare? (Must Have Correct Spelling)')
            stock1 = input('Stock 1: ').upper()
            stock2 = input('Stock 2: ').upper()

            #Grab Timeframe
            print()
            print('1d\n5d\n1mo\n3mo\n6mo\n1y\n2y\n5y\n10y\nytd\nmax')
            print()
            time_frame = input("What Time Frame Would You Like To Analyze?: ")

            #Data Handling
            try:
                #Loading Ticker
                stock1_loaded = yf.Ticker(stock1)
                stock2_loaded = yf.Ticker(stock2)
                print()

                #Showing Stocks
                print(stock1_loaded)
                print(stock2_loaded)

                #Grabbing Data
                stock1_data = stock1_loaded.history(period=time_frame)
                stock2_data = stock2_loaded.history(period=time_frame)

                #printing info about company
                country1 = stock1_loaded.info['country']
                sector1 = stock1_loaded.info['sector']
                country2 = stock2_loaded.info['country']
                sector2 = stock2_loaded.info['sector']
                print()
                print('Simple Company Information:')
                print('Company 1')
                print(sector1)
                print(country1)
                print()
                print('Company 2')
                print(sector2)
                print(country2)

                print()

                #Get revenue
                print(f'Total Revenue for {stock1} and {stock2}')
                income_statement1 = stock1_loaded.financials
                revenue1 = income_statement1.loc["Total Revenue"]
                income_statement2 = stock2_loaded.financials
                revenue2 = income_statement2.loc["Total Revenue"]
                print(stock1)
                print(revenue1)
                print()
                print(stock2)
                print(revenue2)

                print()
                #What is being compared
                print('Open')
                print('High')
                print('Low')
                print('Close')
                print('Volume')
                print('Dividends')
                print('Stock Splits')
                comparing_task = input('Choose what you want to compare from the list above: ').title()

                #plotting
                fig, ax1 = plt.subplots(figsize=(10, 5))
                # Y axis 1
                ax1.plot(stock1_data.index, stock1_data[comparing_task], label=f"{stock1} {comparing_task}", color="r", marker='o')
                ax1.set_xlabel("Date")
                ax1.set_ylabel(f"{stock1} {comparing_task}")
                ax1.tick_params(axis='y', labelcolor='r')
                # Y axis 2
                ax2 = ax1.twinx()
                ax2.plot(stock2_data.index, stock2_data[comparing_task], label=f"{stock2} {comparing_task}", color="b", marker='x')
                ax2.set_ylabel(f"{stock2} {comparing_task}")
                ax2.tick_params(axis='y', labelcolor='b')
                #rest
                plt.title(f"{stock1} vs {stock2} {comparing_task}")
                ax1.grid()
                plt.legend(loc = 'upper left')
                plt.show()

            #Error Handling
            except Exception as e:
                print()
                print(f'Unexpected error: {e}')
                print()
        compare()

#Custom/Error Handling
    else:
        print()
        print(f'You Are Now Viewing {stock_question}')

        print()

        def custom():
            print('1d\n5d\n1mo\n3mo\n6mo\n1y\n2y\n5y\n10y\nytd\nmax')
            print()
            time_frame = input("What Time Frame Would You Like To Analyze?: ")
            try:
                with pd.option_context('display.max_rows', None, 'display.max_columns', None):
                    #Getting Stock
                    custom = stock_question
                    stock = yf.Ticker(custom)
                    print(stock)
                    print()
                    stock_data = stock.history(period=time_frame)
                    print('If there is Dividends or Stock Splits, it will print under this line:')
                    print(stock.actions)

                    #printing info about company
                    country = stock.info['country']
                    sector = stock.info['sector']
                    print()
                    print(sector)
                    print(country)

                    print()

                    #printing stock data
                    print(stock_data)

                    print()

                    #Get revenue
                    print('Total Revenue')
                    income_statement = stock.financials
                    revenue = income_statement.loc["Total Revenue"]
                    print(revenue)

                    #Graphing
                    print()
                graph_question = input('Would You Like to See This Stock Graphed? (y/n): ')
                if graph_question == 'y':
                    plt.figure(figsize=(10, 5))
                    plt.plot(stock_data.index, stock_data['Open'], label=f"{custom} Opening Price", color="r", marker = 'o')
                    plt.plot(stock_data.index, stock_data['Close'], label=f"{custom} Closing Price", color="b", marker = 'o')
                    plt.xlabel("Date")
                    plt.ylabel("Price (USD)")
                    plt.title(f"{custom} Stock Price Over Time")
                    plt.legend()
                    plt.grid()
                    plt.show()
                elif graph_question == 'n':
                    print()

            except Exception as e:
                print()
                print(f'Unexpected error: {e}')
        custom()