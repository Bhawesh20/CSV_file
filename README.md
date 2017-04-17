# CSV_file
Its a program that accepts a price file of baby products(format below) as CSV file, and a list of products that someone wants to buy, and outputs the shop they should go to, and the total price it will cost them.

#Problem Statement

Write a program that accepts a price file of baby products(format below) as CSV file, and a list of products that someone wants to buy, and outputs the shop they should go to, and the total price it will cost them. It is okay to purchase extra products, as long as the total cost is minimized.
price file format
shop ID, price, product 1 label (single product)
shop ID, price, product 1 label, product 2 label, ... (combo packs with multiple products)
Shop IDs are integers, all products are lower case letters and underscores, and the price is a decimal number.

#Sample Data set:

Data File Name = data.csv

1,4.00,teddy_bear   
1,8.00,baby_powder  
2,5.00,teddy_bear  
2,6.50,baby_powder  
3,4.00,pampers_diapers  
3,8.00,johnson_wipes  
4,5.00,johnson_wipes  
4,2.50,cotton_buds  
5,4.00,bath_towel  
5,8.00,scissor  
6,5.00,scissor  
6,6.00,bath_towel,cotton_balls,powder_puff   
  
#Examples/ Sample Test Cases:  
  
Program Input:->  
program data.csv teddy_bear baby_powder  
Expected Output:->  
=> 2, 11.5  
  
Program Input:->  
program data.csv pampers_diapers baby_soap  
Expected Output:->  
=> none  
  
Program Input:->  
program data.csv scissor bath_towel  
Expected Output:->  
=> 6, 11.0  
  
Program Input:->  
program data.csv scissor bath_towel powder_puff  
Expected Output:->
=> 6, 11.0

#Programming Language used:       

Python 3
