# MODULE 9: Surf's Up with Advanced Data Storage and Retrieval

In this lesson, I'll learn about SQLite, a smaller, quicker version of SQL that doesn't require users because it exists on a computer or mobile device. Additionally, we'll study SQLAlchemy, a query tool created for SQLite that combines data frame analysis with statistical analysis. Finally, we'll learn about Flask. a website building framework that makes use of Python.

The most used database engine worldwide is SQLite. In addition to being employed in computers and smartphones, it is also utilized in a number of likely-familiar applications. like Photoshop and iTunes. Because SQLite may be kept locally rather than on a database server, this is one of the main factors contributing to its popularity. As you may guess, it's not always very handy to set up a SQL database server merely to try things out. Local databases offer rapid testing and easy prototyping. Therefore, having the ability to use SQLite to do tasks more rapidly is really beneficial.

I'll utilize the SQLAlchemy query tool, which enables us to query SQLite databases, in order to fully take use of SQLite.

To sum up and convey our analysis I'll go to Flask now. a web framework that will instantly show your analysis on a website. Because you frequently want to share analysis with people who don't want to execute your code themselves, this is really useful.

I'll construct my route and my app, and I'll be ready to go.

## Overview of the Analysis

While on vacation in Hawaii last year I discovered a newfound passion for surfing. I've been trying to come up with a plan that will let me not just return to Hawaii but live here forever. I finally came up with an idea that I think is foolproof. A Surf n' Shake shop serving surfboards and ice cream to locals, tourists, and of  course myself. 

I have some savings I am willing to invest, but I will need some real investor backing to get this off the ground. So after putting together a strong business plan I reached out to an investor: “W. Avy” who is famous for his love of surfing.

My first meeting with him went extremely well but he had one concern: “What about the weather?” He's extremely serious about this. He invested in a surf shop early in his career. However, he didn't ask for any weather analysis and that early venture was rained out of existence.

W. Avy knows I've been learning how to properly analyze data and asks if I can run some analytics on a weather dataset he has from the very island where I'd like to open my shop: The beautiful Oahu. And so, Aloha, Let's go!

### Purpose 
* Bring W. Avy on board convincing him we can properly manage weather using data.

## Results of the Analysis

**Image 1. Summary Statistics for June**

![Captura de Pantalla 2022-03-06 a la(s) 21 49 52](https://user-images.githubusercontent.com/65054637/156968840-affc60b7-c76c-411a-9b9d-3185a1f39ebd.png)

**Image 2. Summary Statistics for December**

![Captura de Pantalla 2022-03-06 a la(s) 21 50 17](https://user-images.githubusercontent.com/65054637/156968831-11c9ac34-9b40-4c30-91ac-a2d5f0a7bc06.png)

As seen from Image 1. Summary Statistics for June and Image 2. Summary Statistics for December, I can conclude the following:

1. There are 183 more observations for June than December (~10% more data). With this datum I can conclude that my data is not considerably biased towards a certain month and conclusions drawn for this data can help us generalize.
2. Mean temperature for these two months where temperatures reach peak high and peak lows during the year are not considerably too different. This suggests that tourists wouldn’t be melting during the summer and freezing during the winter. 
3. From the standard deviation I can conclude that weather is relatively stable during these high season months.

## Summary of the Analysis

- Weather in peak seasons are not that different between each other
- Weather is relatively stable. 
- Max highs in June and December are not considerably different between each other. Nevertheless, max low can reach 10 ºF less than in June, but on average.
