#!/usr/bin/env python
# coding: utf-8

# In[2]:


#pip install matplotlib-venn


# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib_venn import venn3


# | Grupos | Total |
# | :- | -: |
# | Social (100) | 122 |
# | Health (010) | 0 |
# | Exact (001) | 0 |
# | Social & Health (110) | 104 |
# | Social & Physical (101)| 25 |
# | Health & Physical (011) | 0 |
# | Social & Health & Physical (111)| 9 |

# In[9]:


plt.rcParams["figure.figsize"] = (20,10)

df = pd.DataFrame({'Areas': ['Social', 'Social & Health*', 'Social & Physical', "Social & Health* & Physical"],
                   'Manuscripts': [122, 104, 25,9]}, 
                  columns = ['Areas', 'Manuscripts'])

v3 = venn3(subsets = {'100':df.loc[0, 'Manuscripts'],
                      '110':df.loc[1, 'Manuscripts'],
                      '101':df.loc[2, 'Manuscripts'],
                      '111':df.loc[3, 'Manuscripts']},
          set_labels = ('Social Sciences','',''))

v3.get_patch_by_id('100').set_color('yellow')
v3.get_patch_by_id('110').set_color('red')
v3.get_patch_by_id('101').set_color('blue')
v3.get_patch_by_id('111').set_color('green')

v3.get_patch_by_id('100').set_edgecolor('none')
v3.get_patch_by_id('110').set_edgecolor('none')
v3.get_patch_by_id('101').set_edgecolor('none')
v3.get_patch_by_id('111').set_edgecolor('none')

v3.get_label_by_id('100').set_text('%s\n%d\n(%.0f%%)' % (df.loc[0, 'Areas'],
                                                         df.loc[0, 'Manuscripts'],np.divide(df.loc[0, 'Manuscripts'],
                                                                                            df.Manuscripts.sum())*100))

v3.get_label_by_id('110').set_text('%s\n%d\n(%.0f%%)' % (df.loc[1, 'Areas'],
                                                         df.loc[1, 'Manuscripts'],np.divide(df.loc[1, 'Manuscripts'],
                                                                                            df.Manuscripts.sum())*100))

v3.get_label_by_id('101').set_text('%s\n%d\n(%.0f%%)' % (df.loc[2, 'Areas'],
                                                         df.loc[2, 'Manuscripts'],np.divide(df.loc[2, 'Manuscripts'],
                                                                                            df.Manuscripts.sum())*100))

v3.get_label_by_id('111').set_text('%s\n%d\n(%.0f%%)' % (df.loc[3, 'Areas'],
                                                         df.loc[3, 'Manuscripts'],np.divide(df.loc[3, 'Manuscripts'],
                                                                                            df.Manuscripts.sum())*100))
plt.rcParams.update({'font.size': 22})

plt.show()


# ### Reference:
# [jingwen-z.github.io](https://jingwen-z.github.io/data-viz-with-matplotlib-series6-venn-diagram/)
