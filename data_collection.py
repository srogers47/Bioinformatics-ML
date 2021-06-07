#!/usr/bin/env python3 

import pandas as pd 
from chembl_webresource_client.new_client import new_client 

#Target search chembl database  
target_query = new_client.target.search("coronavirus") #Returns dict 
targets = pd.DataFrame.from_dict(target_query) 
print(targets) 
#Select bioactivity data for coronavirus sars 3.
selected_target = targets.target_chembl_id[4] 
print(selected_target) 
#Filter by IC50 to maintain consistency in bioactivity units 
results = new_client.activity.filter(target_chembl_id=selected_target).filter(standard_type="IC50") 
results_df = pd.DataFrame.from_dict(results) 
#NOTE: In results_df, standard_value column measures potency/reaction.
print(results_df) 
