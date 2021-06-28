# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd


class VkPipeline:
    def open_spider(self,spider):
        self.data = dict()
        

    def close_spider(self,spider):
        tags = []
        counts = []
        for tag,count in self.data.items():
            tags.append(tag) 
            counts.append(count)


        dataframe = pd.DataFrame({'Название тега':tags,'Количество':counts})


        writer = pd.ExcelWriter('./data.xlsx',engine='xlsxwriter')
        dataframe.to_excel(writer,sheet_name='Лист1',index=False)

        writer.sheets['Лист1'].set_column('A:A',50)
        writer.sheets['Лист1'].set_column('B:B',30)

        writer.save()


    def process_item(self, item, spider):
        self.data.setdefault(item['data'],0)
        self.data[item['data']]+=1



        
