function Update_Chart_data()
        {
            $.getJSON("./GetOrderCapacity_sp_getOrderCapacityList?Year_Month_Date=" + @DateTime.Now.ToString("yyyyMMdd"), null, function (data) {

            //循環加入資料庫現有資料至各個獨立陣列中
            $.each(data, function (i, itemvalue) {
                //debug用
                //儲存工單號
                Order_No_sp[i] = itemvalue.Key;
                //取得資料庫的sp_DailyProductionList資料表Product_Name值
                Split_str_count = (itemvalue.Value).indexOf("~");
                Product_capacity_sp[i] = itemvalue.Value.slice(0, Split_str_count - 1);
                ////去除最後一個空格 \s代表空格(轉譯) *表示一个或多个空白字符 $代表結束字元
                //Product_Name_Show[i] = Product_Name_Show[i].replace(/\s*$/, "");

                //取得資料庫的sp_DailyProductionList資料表ERP_Part_No

                Real_capacity_sp[i] = itemvalue.Value.slice(Split_str_count + 1);
                ////去除最後一個空格 \s代表空格(轉譯) *表示一个或多个空白字符 $代表結束字元
                //ERP_Part_No_Show[i] = ERP_Part_No_Show[i].replace(/\s*$/, "");

                ////取得資料庫的sp_dailyproductionlist資料表date，並且只針對日來做取出動作
                //split_str_count_2 = (itemvalue.value).indexof("$");
                ////得到年月日
                //date_daily_report[i] = itemvalue.value.slice(split_str_count_1 + 1, split_str_count_2 - 1);

                ////取得資料庫的的sp_dailyproductionlist資料表floor資料
                //split_str_count_4 = (itemvalue.value).indexof("#");
                //floor_daily_report[i] = itemvalue.value.slice(split_str_count_2 + 1, split_str_count_4 - 1);

                ////取得資料庫的sp_dailyproductionlist資料表line_type資料
                //split_str_count_5 = (itemvalue.value).indexof("&");
                //line_type_daily_report[i] = itemvalue.value.slice(split_str_count_4 + 1, split_str_count_5 - 1);

                ////取得資料庫的sp_dailyproductionlist資料表vision資料
                //split_str_count_6 = (itemvalue.value).indexof("%");
                //vision_sp_dailyproductionlist__report[i] = itemvalue.value.slice(split_str_count_5 + 1, split_str_count_6 - 1);

                ////取得資料庫的sp_dailyproductionlist資料表principal
                //split_str_count_8 = (itemvalue.value).indexof("/");
                //principal_daily_report[i] = itemvalue.value.slice(split_str_count_6 + 1, split_str_count_8 - 1);


                ////取得資料庫的sp_dailyproductionlist資料表target_capacity
                //split_str_count_9 = (itemvalue.value).indexof("]");
                //target_capacity_daily_report[i] = itemvalue.value.slice(split_str_count_8 + 1, split_str_count_9 - 1);

                ////production_schedule_id_backup_show[i] = production_schedule_id_show[i];
                ////取得資料庫的sp_dailyproductionlist資料表actual_capacity
                //split_str_count_10 = (itemvalue.value).indexof("^");
                //actual_capacity_daily_report[i] = itemvalue.value.slice(split_str_count_9 + 1, split_str_count_10 - 1);

                ////取得資料庫的sp_dailyproductionlist資料表people
                //split_str_count_11 = (itemvalue.value).indexof("*");
                //people_daily_report[i] = itemvalue.value.slice(split_str_count_10 + 1, split_str_count_11 - 1);

                ////取得資料庫的sp_dailyproductionlist資料表planning_time
                //split_str_count_12 = (itemvalue.value).indexof("<");
                //planning_time_daily_report[i] = itemvalue.value.slice(split_str_count_11 + 1, split_str_count_12 - 1);

                ////取得資料庫的sp_dailyproductionlist資料表cumulative_time
                //split_str_count_13 = (itemvalue.value).indexof(">");
                //cumulative_time_daily_report[i] = itemvalue.value.slice(split_str_count_12 + 1, split_str_count_13 - 1);

                ////取得資料庫的sp_dailyproductionlist資料表work_order_volume
                //split_str_count_14 = (itemvalue.value).indexof("?");
                //work_order_volume_daily_report[i] = itemvalue.value.slice(split_str_count_13 + 1, split_str_count_14 - 1);

                ////取得資料庫的sp_dailyproductionlist資料表arrange_date
                //split_str_count_15 = (itemvalue.value).indexof("|");
                //arrange_date_daily_report[i] = itemvalue.value.slice(split_str_count_14 + 1, split_str_count_15 - 1);

                ////取得資料庫的sp_dailyproductionlist資料表note
                //split_str_count_16 = (itemvalue.value).indexof("+");
                //note_daily_report[i] = itemvalue.value.slice(split_str_count_15 + 1, split_str_count_16 - 1);

                ////取得資料庫的sp_dailyproductionlist資料表work_order
                //work_order_daily_report[i] = itemvalue.value.slice(split_str_count_16 + 1);

                //讓程式知道有幾筆資料
                //total_have_data_count = i;
                ////此變數改成"have"可以讓下面程式判斷資料庫有該月份的資料存在
                //Have_item = "have";
            });
                //初始化效率二維陣列
                Work_order_length = Work_Order_Daily_Report.length;
                //初始化二維陣列
                Chart_work_effecticent = [];
                //初始化顏色二維陣列
                Chart_Work_order_color = [];
                //
                for (set1 = 0; set1 <= 100; set1++) {
                    Chart_work_effecticent[set1] = new Array();
                    Chart_Work_order_color[set1] = new Array();
                }
                //只針對即時效率做運算 ，因此設work_order_choice=1   (0代表目標效率、1代表實際效率)
                for (var work_order_choice = 1; work_order_choice < 2; work_order_choice++) {
                    //單一行陣列裡面會有Order_No_sp筆資料，看當天有幾比工單要做
                    for (count = 0; count <= Order_No_sp.length; count++) {

                        //計算預估產能，預估產能時間=工單量/目標產能
                        //var Estimate_effecticent = Work_order_volume_Daily_Report[count] / Target_capacity_Daily_Report[count];
                        //實際達成率=預估產能時間/累積時間
                        var really_effecticent = (Real_capacity_sp[count] / Product_capacity_sp[count]) * 100;


                        //將數據放入配對相同的工單號裡放入陣列裡，避免出現該工單數據圖出現在別的工單圖上
                        for (mark_choice = 0; mark_choice < Chart_work_order.length; mark_choice++)
                        {
                            //判斷哪個工單號有對應到
                            if (Order_No_sp[count] == Chart_work_order[mark_choice])
                            {
                                if (really_effecticent != undefined)
                                {
                                    Chart_work_effecticent[work_order_choice][mark_choice] = really_effecticent;
                                }
                                else
                                {
                                    Chart_work_effecticent[work_order_choice][mark_choice] = 0;
                                }

                                // Chart_Bar_work_order[work_order_choice].push(Work_Order_Daily_Report[count]);
                                break;
                            }
                        }
                    }
                }
                //設定圖表Bar顏色
                for (var color_choice = 0; color_choice < Chart_work_effecticent[1].length; color_choice++)
                {
                    //大於90後
                    if (parseFloat(Chart_work_effecticent[1][color_choice]) > 90.00)
                    {
                        Chart_Work_order_color[1][color_choice] ="rgba(13,255,13)";
                    }
                    //介於71~89之間
                    else if (parseFloat(Chart_work_effecticent[1][color_choice]) > 70.00)
                    {
                        Chart_Work_order_color[1][color_choice] = "rgba(255,255,36)";
                    }
                    //小於70後
                    else
                    {
                        Chart_Work_order_color[1][color_choice] = "rgba(255,89,89)";
                    }
                }
                //設定線標籤
                //Chart_Bar_work_order_mark[0] = "目標效率";
                Chart_Bar_work_order_mark[1] = "實際效率";

                //讓資料都可以插入到圖表裡
                for (var chioce_data = 1; chioce_data < 2; chioce_data++)
                {
                    if (Chart_work_effecticent[chioce_data] == "")
                        continue;
                    var color_chart = rgba_random(0.5);
                    //加入現有資料
                    const newBarDataset3 = {
                        //標籤名稱
                        label: Chart_Bar_work_order_mark[chioce_data],
                        //Chart_Work_order_color[chioce_data]
                        backgroundColor: Chart_Work_order_color[1],
                        borderColor: Chart_Work_order_color[1],
                        data: Chart_work_effecticent[chioce_data],
                    };
                    //若不想顯示目標效率的值就把下方chioce_data改為0，並把上方插入圖表的程式碼區塊碼掉
                    myBarChart.data.datasets[0]=newBarDataset3;
                    myBarChart.update();
                }
            });
        }