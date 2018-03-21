import csv

# creation of the output csv file to import in the shop
with open('to_import.csv', 'w', newline='') as csvfile:
    fieldnames = ["ID","Slug","Name","Date Created","Author","Description","Excerpt","Status","Categories","Tags",
    "Price","Files","File Download Limit","Featured Image","SKU","Notes","Sales","Earnings"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

# defining the constant 

file_downloads_limit = ''
featured_image = ''


# opening the source csv file created by the scrapy spiders
with open('spiders\\desc1.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        print(row['title'], row['author'], row['official_sales_page'])
        name = row['title']
        slug = name.replace(" ", "-")
        author = row['author']
        official_sales_page = row['official_sales_page']
        excerpt = " "
        status = "publish"
        categories = row['category']
        tags = row['tags']
        released = row['released']
        price = row['price']
        file_path = "https://topgpl.com/wp-content/uploads/edd/"+slug+".zip"
        file_downloads_limit = ''
        featured_image = "http://topgpl.com/wp-content/uploads/edd/images/"+slug+".jpg"
        SKU = ''
        notes = ''
        sales = ''
        earnings = ''

        print (name+", "+author+", "+official_sales_page)

        desc1 = "<ul><li>You will find exactly the same files in their latest version (Plugin/Theme: "+name+") distributed by "+author+".</li>"
        desc2 = "<li>The price does not include the support or any license keys. That's the reason why it's so affordable (Please read our <a href=\'https://topgpl.com/faq/\'>FAQ</a> for more Informations).</li>"
        desc3 = "<li>Official product page : <a href=\'"+official_sales_page+"\'>"+official_sales_page+"</a></li>"
        desc4 = "<li>TopGPL is not affiliated or in any way related to third-party developers or trademark owners, including: WordPress, WooCommerce, "+author+", etc.</li>"
        desc5 = "<li>Download verified by McAfee Secure</li>"
        desc6 = "<li>30 days money back guarantee, no questions asked.</li>"
        desc7 = "<li>1 year of updates.</li>"
        desc8 = "<li>Join the Members Club and get unlimited downloads to all our themes and plugins for just $15 a month.</li></ul>"
        
        desc = desc1+desc2+desc3+desc4+desc5+desc6+desc7+desc8

        with open('to_import.csv', 'a', newline='') as f:
            fields=['',slug,name,released,author,desc,excerpt,status,categories,tags,price,file_path,file_downloads_limit,featured_image,SKU,notes,sales,earnings]
            writer = csv.writer(f)
            writer.writerow(fields)





    
    
