import panel as pn
import pandas as pd
pn.extension('altair', 'tabulator')
text = pn.widgets.TextInput()

text.value
text.param.value
df = pd.DataFrame({
  'A': [1, 2, 3, 4],
  'B': [10, 20, 30, 40]
})

df_pane = pn.panel(df)
print(pn.Row(df))

pn.pane.DataFrame(df)

df_pane.servable()