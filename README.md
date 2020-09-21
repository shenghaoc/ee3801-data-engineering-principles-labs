# ee3801-data-engineering-principles-labs
My EE3801 Data Engineering Principles lab sumissions

## What I learned from Lab 1
1. In pandas, operations are usually done along an entire axis, therefore there's no need to use a loop.
1. Moreover, a pandas method usually creates a new DataFrame rather than modify the original, making loops extremely expensive.

## What I learned from Lab 2
1. DataFrame and Series can use pyplot methods directly, however the return type is `matplotlib.axes._subplots.AxesSubplot`, so if the pyplot method returns something useful it would be better to use it instead.
