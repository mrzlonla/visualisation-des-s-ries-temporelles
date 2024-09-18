# main.py
from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

# Appeler et générer les trois graphiques
line_fig = draw_line_plot()
bar_fig = draw_bar_plot()
box_fig = draw_box_plot()

# Afficher les figures (optionnel)
line_fig.show()
bar_fig.show()
box_fig.show()
