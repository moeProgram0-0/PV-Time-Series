import time_series_visualizer
from unittest import main
import datetime

print("Programmer: Mamoudou T. Bah")
time = datetime.datetime.now()
print(f"Time Series, {time.strftime('%B %d, %Y @ %H:%M:%S')}")
print("")

# Test your function by calling it here
time_series_visualizer.draw_line_plot()
time_series_visualizer.draw_bar_plot()
time_series_visualizer.draw_box_plot()

# Run unit tests automatically
main(module='test_module', exit=False)