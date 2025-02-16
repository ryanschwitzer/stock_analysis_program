import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import msvcrt

#----------------------------------------------------------------------

#Home Screen
print('Welcome to Ryans Stock Performance Analysis')
print()
print('-----------------------')
print('|    Press any key    |')
print('|     To Continue     |')
print('-----------------------')
print()
msvcrt.getch()
print()

#----------------------------------------------------------------------

#Repeating Loop
while True:
    #Input
    print()
    print('Game Stop (GP)')
    print('Tesla (T)')
    print('Amazon (AZN)')
    print('AMD (AMD)')
    print('Any NASDAQ. (Must Have Correct Spelling)')
    print('Compare Stocks (CS)')
    print('Quit (Q)')
    print()
    stock_question = input('Which Stock Would You like to see data about?: ').upper()

#----------------------------------------------------------------------

#Game Stock | 'GP'
    if stock_question == 'GP':

        print()
        print('GAMESTOP STOCK')

        def gamestop():
            print('1d\n5d\n1mo\n3mo\n6mo\n1y\n2y\n5y\n10y\nytd\nmax')
            time_frame = input("What Time Frame Do you want to show?: ")
            
            with pd.option_context('display.max_rows', None, 'display.max_columns', None):
                #Getting Stock
                gme = yf.Ticker("GME")
                print(gme)
                print()
                gme_data = gme.history(period=time_frame)
                print('If there is Dividends or Stock Splits, it will print under this line:')
                print(gme.actions)

                #printing info about company
                country = gme.info['country']
                sector = gme.info['sector']
                print()
                print('Simple Company Information:')
                print(sector)
                print(country)

                #printing stock data
                print(gme_data)

                print()

                #Get revenue
                print('Total Revenue')
                income_statement = gme.financials
                revenue = income_statement.loc["Total Revenue"]
                print(revenue)
            print()

            #Graphing
            graph_question = input('Would You Like to See This Stock Graphed? (y/n): ')
            if graph_question == 'y':
                plt.figure(figsize=(10, 5))
                plt.plot(gme_data.index, gme_data['Open'], label=f"GME Opening Price", color="r", marker = 'o')                
                plt.plot(gme_data.index, gme_data['Close'], label=f"GME Closing Price", color="b", marker = 'o')
                plt.xlabel("Date")
                plt.ylabel("Price (USD)")
                plt.title(f"GME Stock Price Over Time")
                plt.legend()
                plt.grid()
                plt.show()
            elif graph_question == 'n':
                print()
        gamestop()

#Tesla | 'T'
    elif stock_question == 'T':

        print()
        print('TESLA STOCK')

        def tesla():
            print('1d\n5d\n1mo\n3mo\n6mo\n1y\n2y\n5y\n10y\nytd\nmax')
            time_frame = input("What Time Frame Do you want to show?: ")

            with pd.option_context('display.max_rows', None, 'display.max_columns', None):
                #Getting Stock
                tsla = yf.Ticker("TSLA")
                print(tsla)
                print()
                tsla_data = tsla.history(period=time_frame)
                print('If there is Dividends or Stock Splits, it will print under this line:')
                print(tsla.actions)

                #printing info about company
                country = tsla.info['country']
                sector = tsla.info['sector']
                print()
                print('Simple Company Information:')
                print(sector)
                print(country)

                #printing stock data
                print(tsla_data)

                print()

                #Get revenue
                print('Total Revenue')
                income_statement = tsla.financials
                revenue = income_statement.loc["Total Revenue"]
                print(revenue)
            print()

            #Graphing
            graph_question = input('Would You Like to See This Stock Graphed? (y/n): ')
            if graph_question == 'y':
                plt.figure(figsize=(10, 5))
                plt.plot(tsla_data.index, tsla_data['Open'], label=f"TSLA Opening Price", color="r", marker = 'o')                
                plt.plot(tsla_data.index, tsla_data['Close'], label=f"TSLA Closing Price", color="b", marker = 'o')
                plt.xlabel("Date")
                plt.ylabel("Price (USD)")
                plt.title(f"TSLA Stock Price Over Time")
                plt.legend()
                plt.grid()
                plt.show()
            elif graph_question == 'n':
                print()
        tesla()

#Amazon | 'AZN'
    elif stock_question == 'AZN':
        print()
        print('AMAZON STOCK')

        def amazon():

            print('1d\n5d\n1mo\n3mo\n6mo\n1y\n2y\n5y\n10y\nytd\nmax')
            time_frame = input("What Time Frame Do you want to show?: ")

            with pd.option_context('display.max_rows', None, 'display.max_columns', None):
                #Getting Stock
                amzn = yf.Ticker("AMZN")
                print(amzn)
                print()
                amzn_data = amzn.history(period=time_frame)
                print('If there is Dividends or Stock Splits, it will print under this line:')
                print(amzn.actions)

                #printing info about company
                country = amzn.info['country']
                sector = amzn.info['sector']
                print()
                print('Simple Company Information:')
                print(sector)
                print(country)

                #printing stock data
                print(amzn_data)

                print()

                #Get revenue
                print('Total Revenue')
                income_statement = amzn.financials
                revenue = income_statement.loc["Total Revenue"]
                print(revenue)
            print()

            #Graphing
            graph_question = input('Would You Like to See This Stock Graphed? (y/n): ')
            if graph_question == 'y':
                plt.figure(figsize=(10, 5))
                plt.plot(amzn_data.index, amzn_data['Open'], label=f"AMZN Opening Price", color="r", marker = 'o')                
                plt.plot(amzn_data.index, amzn_data['Close'], label=f"AMZN Closing Price", color="b", marker = 'o')
                plt.xlabel("Date")
                plt.ylabel("Price (USD)")
                plt.title(f"AMZN Stock Price Over Time")
                plt.legend()
                plt.grid()
                plt.show()
            elif graph_question == 'n':
                print()
        amazon()

#AMD | 'AMD'
    elif stock_question == 'AMD':

        print()
        print('AMD STOCK')

        def amd():
            print('1d\n5d\n1mo\n3mo\n6mo\n1y\n2y\n5y\n10y\nytd\nmax')
            time_frame = input("What Time Frame Do you want to show?: ")
            
            with pd.option_context('display.max_rows', None, 'display.max_columns', None):
                #Getting Stock
                amd = yf.Ticker("AMD")
                print(amd)
                print()
                amd_data = amd.history(period=time_frame)
                print('If there is Dividends or Stock Splits, it will print under this line:')
                print(amd.actions)

                #printing info about company
                country = amd.info['country']
                sector = amd.info['sector']
                print()
                print('Simple Company Information:')
                print(sector)
                print(country)

                print()

                #printing stock data
                print(amd_data)

                print()

                #Get revenue
                print('Total Revenue')
                income_statement = amd.financials
                revenue = income_statement.loc["Total Revenue"]
                print(revenue)
            print()

            #Graphing
            graph_question = input('Would You Like to See This Stock Graphed? (y/n): ')
            if graph_question == 'y':
                plt.figure(figsize=(10, 5))
                plt.plot(amd_data.index, amd_data['Open'], label=f"AMD Opening Price", color="r", marker = 'o')                
                plt.plot(amd_data.index, amd_data['Close'], label=f"AMD Closing Price", color="b", marker = 'o')
                plt.xlabel("Date")
                plt.ylabel("Price (USD)")
                plt.title(f"AMD Stock Price Over Time")
                plt.legend()
                plt.grid()
                plt.show()
            elif graph_question == 'n':
                print()
        amd()

#Quit | 'Q'
    elif stock_question == 'Q':
        print()
        print('Thank you for using Ryans Stock Performance Analysis')
        break

    elif stock_question == 'CS':
        print()
        print('COMPARE STOCKS')

        def compare():

            #Grab Stocks
            print('What stocks would you like to compare? (Must Have Correct Spelling)')
            stock1 = input('Stock 1: ').upper()
            stock2 = input('Stock 2: ').upper()

            #Grab Timeframe
            print('1d\n5d\n1mo\n3mo\n6mo\n1y\n2y\n5y\n10y\nytd\nmax')
            time_frame = input("What Time Frame Do you want to show?: ")

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
        print('CUSTOM NASDAQ STOCK')

        def custom():
            print('1d\n5d\n1mo\n3mo\n6mo\n1y\n2y\n5y\n10y\nytd\nmax')
            time_frame = input("What Time Frame Do you want to show?: ")
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
