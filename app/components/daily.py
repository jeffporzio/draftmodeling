from webComponent import WebComponent, WCProperties

title = "Daily"
date = "8/1/2021"

template = "daily.html"

properties = {
     "title": title,
     "date": date
}

daily_properties = WCProperties(properties)
daily_component = WebComponent(properties=daily_properties, template=template)