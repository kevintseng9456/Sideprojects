 function Get_Org_Price(pix_Count, value_price) {
            //要獨立分開取，因為總價錢算出來不同，紀錄也會不同
            // 預估各機種該月到今日總銷售額取資料專用
            if (pix_Count == 1) {
                for (Price_count = 0; Price_count < Product_Month_Date_Sale_Price_proportion.length; Price_count++) {
                    if (value_price == Product_Month_Date_Sale_Price_proportion[Price_count]) {
                        str = Product_Month_Date_Sale_Price_proportion_Org_Price[Price_count];
                        return str;
                    }
                }
            }
            //預估各機種該月總銷售額取資料專用
            else if (pix_Count == 2)
            {
                for (Price_count = 0; Price_count < Product_Month_Sale_Price_proportion.length; Price_count++) {
                    if (value_price == Product_Month_Sale_Price_proportion[Price_count]) {
                        str = Product_Month_Sale_Price_proportion_Org_Price[Price_count];
                        return str;
                    }
                }
            }


        }