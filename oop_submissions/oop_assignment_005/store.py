class Item:
    def __init__(self,name,price,category):
         self._name=name
         if price <= 0:
             raise ValueError("Invalid value for price, got {}".format(price))
         else:
             self._price=price
         self._category=category
   
    def __str__(self):
        return (str(self._name)+"@"+str(self._price)+"-"+str(self._category))
    
    
    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price    

    @property
    def category(self):
        return self._category

class Query:
    con_list=["IN","EQ","GT","GTE","LT","LTE","STARTS_WITH","ENDS_WITH","CONTAINS"]
    
    def __init__(self,field,operation,value):
        self._field = field
        self._value = value
        if operation not in Query.con_list:
            raise ValueError("Invalid value for operation, got {}".format(operation))
        else:
            self._operation =  operation
   
    def __str__(self):
        return ("{} {} {}".format(self._field,self._operation,self._value))
        
    @property
    def field(self):
        return self._field
        
    @property
    def operation(self):
        return self._operation    
        
    @property
    def value(self):
        return self._value
    
        
class Store:
    
    def __init__(self):
        self.store_items=[]
    
    
    def __str__(self):
        if(len(self.store_items)>0):
            return("\n".join(map(str,self.store_items)))
        else:
            return "No items"
            
    
    
    def add_item(self,item):
        self.store_items.append(item)

    
    def filter(self,query):
        filter_list=Store()
       
        for item in self.store_items:

            key=getattr(item,query.field)
            
            if(query.operation  == "IN" and key in query.value):
                filter_list.add_item(item)
            
            elif(query.operation  == "EQ" and key == query.value):
                filter_list.add_item(item)
            
            elif(query.operation  == "GT" and key > query.value):
                filter_list.add_item(item)
            
            elif(query.operation  == "GTE" and key >= query.value):
                filter_list.add_item(item)

            elif(query.operation  == "LT" and key < query.value):
                filter_list.add_item(item)
            
            elif(query.operation  == "LTE" and key <= query.value):
                filter_list.add_item(item)

            elif(query.operation  == "STARTS_WITH" and key.startswith(query.value)):
                filter_list.add_item(item)
            
            elif(query.operation  == "ENDS_WITH" and key.endswith(query.value)):
                filter_list.add_item(item)
            
            elif(query.operation  == "CONTAINS" and query.value in key):
                filter_list.add_item(item)
                
        return filter_list
    
    def count(self):
        return len(self.store_items)

    def exclude(self,query):
        exclude_list=Store()
        filter_query=self.filter(query)
        for item in self.store_items:
            if item not in filter_query.store_items:
                exclude_list.add_item(item)
        return exclude_list        



































































'''for compare_item in result_list:
            key=getattr(compare_item,query.field)
            if(query.operation  == "IN" and key in query.value):
                result_list.append(compare_item)
            
            elif(query.operation  == "EQ" and key in query.value):
                result_list.append(compare_item)
            
            elif(query.operation  == "GT" and key in query.value):
                result_list.append(compare_item)
            
            elif(query.operation  == "GTE" and key in query.value):
                result_list.append(compare_item)

            elif(query.operation  == "LT" and key in query.value):
                result_list.append(compare_item)
            
            elif(query.operation  == "LTE" and key in query.value):
                result_list.append(compare_item)

            elif(query.operation  == "STARTS_WITH" and key in query.value):
                result_list.append(compare_item)
            
            elif(query.operation  == "ENDS_WITH" and key in query.value):
                result_list.append(compare_item)
            
            elif(query.operation  == "CONTAINS" and key in query.value):
                result_list.append(compare_item)'''
    
    