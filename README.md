# Databasecs4111


The URL of your web application: http://35.238.168.24:8111/index 

A description of the parts of your original proposal in Part 1 that you implemented, the parts you did not 
we successed in login and signup, search on the index page, show hotsearch, order and pay, and user can see the oder detail on his homepage.

Briefly describe two of the web pages that require (what you consider) 
the most interesting database operations in terms of what the pages are used for, 
how the page is related to the database operations (e.g., inputs on the page are used in such and such way to produce database operations that do such and such), 
and why you think they are interesting.

The most interesting page is index and pay.
For index:we have three things shown on the page：hot_search_list，product_list，brand_list to show different type of keywords
select_sql = '''SELECT key_word,product_id FROM hotsearched WHERE searched_rank <= 10 ORDER BY searched_rank'''
select_sql = '''SELECT product_id, name, price, unit, is_shipfree FROM product WHERE isdelete = false'''
select_sql = '''SELECT DISTINCT b.brand_id, b.brand_name FROM brand b  WHERE EXISTS (SELECT * FROM product p WHERE p.brand_id=b.brand_id)'''
 
For pay: we firstly use sql to check if this user has login, if he has, we will use request form to get the information user give, 
then update our database,  and show the update on user homepage.
