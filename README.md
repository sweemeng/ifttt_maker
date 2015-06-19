What is this
=============

This is a simple python module to trigger event to IFTTT Maker channel

Example
--------

```python
import ifttt_maker

ifttt = ifttt_maker.Ifttt("event_name", "secret key")
ifttt.trigger(value1="value1", value2="value2", value3="value3")

```
