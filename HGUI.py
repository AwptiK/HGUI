import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject
import math


modes = ["Year", "Array", "Date"]
hijri_entry_modes = ["Enter Hijri Year", "Enter Start Year", "Enter Hijri Day"]
gregorian_entry_modes = ["Enter Gregorian Year", "Enter End Year", "Enter Gregorian Day"]

def int_part(floatNum):
    if floatNum < -0.0000001: return math.ceil(floatNum - 0.0000001)
    return math.floor(floatNum + 0.0000001)


def gregorian_to_hijri(year, month, day):

        jd1 = int_part((1461 * (year + 4800 + int_part((month - 14) / 12.0))) / 4)
        jd2 = int_part((367 * (month - 2 - 12 *  (int_part((month - 14) /
        12.0)))) / 12)
        jd3 = int_part((3 * (int_part((year + 4900 + int_part((month - 14) /
        12.0)) / 100))) / 4)
        jd = jd1 + jd2 - jd3 + day - 32075

        l = jd - 1948440 + 10632
        n = int_part((l - 1) /10631.0)
        l = l - 10631 * n + 354

        j1 = (int_part((10985 - l) / 5316.0)) * (int_part((50 * l) / 17719.0))
        j2 = (int_part(l / 5670.0)) * (int_part((43 * l) / 15238.0))
        j = j1 + j2

        l1 = (int_part((30 - j) / 15.0)) * (int_part((17719 * j) / 50.0))
        l2 = (int_part(j / 16.0)) * (int_part((15238 * j) / 43.0))
        l = l - l1 - l2 + 29


        m = int_part((24 * l) / 709.0)
        y = 30 * n + j - 30
        d = l - int_part((709 * m) / 24.0)
        return [m, d, y]

def hijri_to_gregorian(year, month, day):
    jd1 = int_part((11 * year + 3) / 30.0)
    jd2 = int_part((month - 1) / 2.0)
    jd = jd1 + 354 * year + 30 * month - jd2 + day + 1948440 - 385


    l = jd + 68569
    n = int_part((4 * l) / 146097.0)
    l = l - int_part((146097 * n + 3) / 4.0)
    i = int_part((4000 * (l + 1)) / 1461001.0)
    l = l - int_part((1461 * i) / 4.0) + 31
    j = int_part((80 * l) / 2447.0)
    d = l - int_part((2447 * j) / 80.0)
    l = int_part(j / 11.0)
    m = j + 2 - 12 * l
    y = 100 * (n - 49) + i + l
    return m, d, y

def convert_to_gregorian(year, gregorian_entry):
    year = float(year)
    year = (year * 0.97) + 622;
    gregorian_entry.set_text(str(int(year)))

def convert_to_hijri(year, hijri_entry):
    year = float(year)
    year = (year - 622) * 1.03;
    hijri_entry.set_text(str(int(year)))    

def clear():
    for i in range(0, 2):
        gregorian_entry = builder.get_object("gregorian_entry")
        gregorian_combo_box = builder.get_object("gregorian_combo_box")
        gregorian_year_entry = builder.get_object("gregorian_year_entry")
        gregorian_combo_box.set_sensitive(True)
        gregorian_year_entry.set_sensitive(True)
        gregorian_entry.set_sensitive(True)
        gregorian_combo_box.set_active_iter(None)
        gregorian_entry.set_text('')    
        gregorian_year_entry.set_text('')
        hijri_entry = builder.get_object("hijri_entry")
        hijri_combo_box = builder.get_object("hijri_combo_box")
        hijrii_year_entry = builder.get_object("hijri_year_entry")
        hijri_combo_box.set_sensitive(True)
        hijrii_year_entry.set_sensitive(True)
        hijri_entry.set_sensitive(True)
        hijri_combo_box.set_active_iter(None)
        hijri_entry.set_text('')
        hijrii_year_entry.set_text('')


class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

    # def on_window1_action_added(self, window):
    #     show_list_button = builder.get_object("show_list_button")
    #     show_list_button.set_sensitive(True)

    global gregorian_day
    gregorian_day = 0
    def on_gregorian_entry_value_changed(self, spinbutton):
        global gregorian_day
        if(index == 1):
            return
        gregorian_day = spinbutton.get_text()
        hijri_entry = builder.get_object("hijri_entry")
        hijri_combo_box = builder.get_object("hijri_combo_box")
        hijrii_year_entry = builder.get_object("hijri_year_entry")
        hijri_combo_box.set_sensitive(False)
        hijrii_year_entry.set_sensitive(False)
        hijri_entry.set_sensitive(False)
        print(gregorian_day)

    global hijri_day
    hijri_day = 0
    def on_hijri_entry_value_changed(self, spinbutton):
        global hijri_day
        if(index == 1):
            return
        hijri_day = spinbutton.get_text()
        gregorian_entry = builder.get_object("gregorian_entry")
        gregorian_combo_box = builder.get_object("gregorian_combo_box")
        gregorian_year_entry = builder.get_object("gregorian_year_entry")
        gregorian_combo_box.set_sensitive(False)
        gregorian_year_entry.set_sensitive(False)
        gregorian_entry.set_sensitive(False)
        print(hijri_day)

    global gregorian_month
    gregorian_month = 0
    def on_gregorian_combo_box_changed(self, combobox):
        global gregorian_month
        gregorian_month = combobox.get_active() + 1
        hijri_entry = builder.get_object("hijri_entry")
        hijri_combo_box = builder.get_object("hijri_combo_box")
        hijrii_year_entry = builder.get_object("hijri_year_entry")
        hijri_combo_box.set_sensitive(False)
        hijrii_year_entry.set_sensitive(False)
        hijri_entry.set_sensitive(False)
        print(gregorian_month)


    global hijri_month
    hijri_month = 0
    def on_hijri_combo_box_changed(self, combobox):
        global hijri_month
        hijri_month = combobox.get_active() + 1
        gregorian_entry = builder.get_object("gregorian_entry")
        gregorian_combo_box = builder.get_object("gregorian_combo_box")
        gregorian_year_entry = builder.get_object("gregorian_year_entry")
        gregorian_combo_box.set_sensitive(False)
        gregorian_year_entry.set_sensitive(False)
        gregorian_entry.set_sensitive(False)
        print(hijri_month)  

    global hijri_year
    hijri_year = 0
    def on_hijri_year_entry_value_changed(self, entry):
        global hijri_year
        hijri_year = entry.get_text()
        gregorian_entry = builder.get_object("gregorian_entry")
        gregorian_combo_box = builder.get_object("gregorian_combo_box")
        gregorian_year_entry = builder.get_object("gregorian_year_entry")
        gregorian_combo_box.set_sensitive(False)
        gregorian_year_entry.set_sensitive(False)
        gregorian_entry.set_sensitive(False)
        print(hijri_year)

    global gregorian_year
    gregorian_year = 0
    def on_gregorian_year_entry_value_changed(self, entry):
        global gregorian_year
        gregorian_year = entry.get_text()
        hijri_entry = builder.get_object("hijri_entry")
        hijri_combo_box = builder.get_object("hijri_combo_box")
        hijrii_year_entry = builder.get_object("hijri_year_entry")
        hijri_combo_box.set_sensitive(False)
        hijrii_year_entry.set_sensitive(False)
        hijri_entry.set_sensitive(False)
        print(gregorian_year)        

    def on_popup2_close_button_clicked(self, button):
        popup2 = builder.get_object("popup2")
        popup2.hide()
        convert_button.set_sensitive(True)

    def on_gregorian_entry_focus_in_event(self, entry, data):
        hijri_entry = builder.get_object("hijri_entry")
        if(index == 0):
            hijri_entry.set_sensitive(False)
        elif(index == 1):
            hijri_entry.set_sensitive(True)
        else:
            hijri_entry.set_sensitive(True)

    def on_hijri_entry_focus_in_event(self, entry, data):
        gregorian_entry = builder.get_object("gregorian_entry")
        if(index == 0):
            gregorian_entry.set_sensitive(False)
        elif(index == 1):
            gregorian_entry.set_sensitive(True)
        else:    
            gregorian_entry.set_sensitive(True)
   

    def on_popup_window_close_button_clicked(self, button):
        popup = builder.get_object("popup")
        popup.hide()

    def on_show_list_button_clicked(self, button):
        popup = builder.get_object("popup")
        popup.show_all()

    def on_clear_button_clicked(self, button):
        hijri_entry = builder.get_object("hijri_entry")
        gregorian_entry = builder.get_object("gregorian_entry")
        hijri_entry.set_sensitive(True)
        gregorian_entry.set_sensitive(True)
        clear()
        convert_button = builder.get_object("convert_button")    
        convert_button.set_sensitive(True)

    global index
    index = 0
    def on_switch_modes_button_clicked(self, button):
        global index
        button = builder.get_object("switch_modes_button")
        index += 1
        if(index >= 3):
            index = 0
        button.set_label(modes[index])
        hijri_entry = builder.get_object("hijri_entry")
        gregorian_entry = builder.get_object("gregorian_entry")
        hijri_year_entry = builder.get_object("hijri_year_entry")
        gregorian_year_entry = builder.get_object("gregorian_year_entry")
        hijri_combo_box = builder.get_object("hijri_combo_box")
        gregorian_combo_box = builder.get_object("gregorian_combo_box")
        hijri_entry.set_placeholder_text(hijri_entry_modes[index])
        gregorian_entry.set_placeholder_text(gregorian_entry_modes[index])
        clear()
        convert_button = builder.get_object("convert_button")
        show_list_button = builder.get_object("show_list_button")
        gregorian_adjustment = builder.get_object("adjustment2")
        if(modes[index] == "Year"):
            convert_button.disconnect_by_func(self.on_convert_button_clicked_3)
            convert_button.connect("clicked", self.on_convert_button_clicked)
            show_list_button.set_sensitive(False)
            gregorian_adjustment.set_lower(622)
            hijri_year_entry.hide()
            gregorian_year_entry.hide()
            hijri_combo_box.hide()
            gregorian_combo_box.hide()
            hijri_entry.set_tooltip_markup("Set Hijri Year")
            gregorian_entry.set_tooltip_markup("Set Gregorian Year")
        elif(modes[index] == "Array"):
            convert_button.disconnect_by_func(self.on_convert_button_clicked)
            convert_button.connect("clicked", self.on_convert_button_clicked_2)
            hijri_entry.set_sensitive(True)
            gregorian_entry.set_sensitive(True)
            show_list_button.set_sensitive(True)
            gregorian_adjustment.set_lower(0)
            hijri_year_entry.hide()
            gregorian_year_entry.hide()
            hijri_combo_box.hide()
            gregorian_combo_box.hide()
            hijri_entry.set_tooltip_markup("Set Starting Year")
            gregorian_entry.set_tooltip_markup("Set Ending Year")
        elif(modes[index] == "Date"):
            convert_button.disconnect_by_func(self.on_convert_button_clicked_2)
            convert_button.connect("clicked", self.on_convert_button_clicked_3)
            hijri_entry.set_sensitive(True)
            gregorian_entry.set_sensitive(True)
            show_list_button.set_sensitive(False)
            gregorian_adjustment.set_lower(0)
            hijri_year_entry.show_all()
            gregorian_year_entry.show_all()   
            hijri_combo_box.show_all()
            gregorian_combo_box.show_all() 
            hijri_entry.set_tooltip_markup("Set Hijri Day")
            gregorian_entry.set_tooltip_markup("Set Gregorian Day")
            hijri_year_entry.set_tooltip_markup("Set Hijri Year")
            gregorian_year_entry.set_tooltip_markup("Set Gregorian Year")
            hijri_combo_box.set_tooltip_markup("Select Hijri Month")
            gregorian_combo_box.set_tooltip_markup("Select Gregorian Month")

        clear()
        convert_button.set_sensitive(True)
        print("switched " + str(index))


    def on_convert_button_clicked(self, button):
        hijri_entry = builder.get_object("hijri_entry")
        gregorian_entry = builder.get_object("gregorian_entry")
        
        if(hijri_entry.get_text() != ''):
            convert_to_gregorian(hijri_entry.get_text(), gregorian_entry)
        elif(gregorian_entry.get_text() != ''):
            convert_to_hijri(gregorian_entry.get_text(), hijri_entry)  
        else:
            popup2 = builder.get_object("popup2")
            popup2.show_all()
            print("NO")    

        convert_button = builder.get_object("convert_button")    
        convert_button.set_sensitive(False)    

    def on_convert_button_clicked_2(self, button):
        hijri_entry = builder.get_object("hijri_entry")
        gregorian_entry = builder.get_object("gregorian_entry")

        if(gregorian_entry.get_text() == '' or hijri_entry.get_text() == ''):
            popup2 = builder.get_object("popup2")
            popup2.show_all()
            print("NO")    
            return

        starting_year = int(float(hijri_entry.get_text()))
        ending_year = int(float(gregorian_entry.get_text()))
        list_view = builder.get_object("list_view")

        
        year_array = range(starting_year, ending_year + 1)

        for element in list_view.get_children():
            element.destroy()

        for x in year_array:
            y = (x * 0.97) + 622
            row = Gtk.ListBoxRow()
            hbox = Gtk.Box()
            row.add(hbox)
            item_label = Gtk.Label()
            item_label.set_margin_top(6)
            item_label.set_margin_bottom(6)
            item_label.set_margin_start(6)
            item_label.set_margin_end(6)
            item_label.set_markup(str(x) + " Hijri is " + str(int(y)) + " Gregorian".format(32))
            hbox.pack_start(item_label, True, True,0)
            list_view.add(row)

        show_list_button = builder.get_object("show_list_button")
        show_list_button.clicked()
        convert_button.set_sensitive(False)    

    def on_convert_button_clicked_3(self, button):
        hijri_combo_box = builder.get_object("hijri_combo_box")
        gregorian_combo_box = builder.get_object("gregorian_combo_box")

        hijri_entry = builder.get_object("hijri_entry")
        gregorian_entry = builder.get_object("gregorian_entry")
        
        hijri_year_entry = builder.get_object("hijri_year_entry")
        gregorian_year_entry = builder.get_object("gregorian_year_entry")

        if(hijri_entry.get_text() != '' and hijri_combo_box.get_active() is not None and hijri_year_entry.get_text() != ''):
            date = hijri_to_gregorian(int(hijri_year), int(hijri_month), int(hijri_day))
            gregorian_combo_box.set_active(date[0] - 1)
            gregorian_entry.set_text(str(date[1]))
            gregorian_year_entry.set_text(str(date[2]))
        elif(gregorian_entry.get_text() != '' and gregorian_combo_box.get_active() is not None and gregorian_year_entry.get_text() != ''):
            date = gregorian_to_hijri(int(gregorian_year), int(gregorian_month), int(gregorian_day))
            hijri_combo_box.set_active(date[0] - 1)
            hijri_entry.set_text(str(date[1]))
            hijri_year_entry.set_text(str(date[2]))
        else:
            popup2 = builder.get_object("popup2")
            popup2.show_all()
            print("NO")    

        convert_button.set_sensitive(False)    
        print(date[0], date[1], date[2])


builder = Gtk.Builder()
builder.add_from_file("HGUI.glade")
builder.connect_signals(Handler())


window = builder.get_object("window1")

convert_button = builder.get_object("convert_button")    
hijri_combo_box = builder.get_object("hijri_combo_box")
hijri_year_entry = builder.get_object("hijri_year_entry")
gregorian_combo_box = builder.get_object("gregorian_combo_box")
gregorian_year_entry = builder.get_object("gregorian_year_entry")
show_list_button = builder.get_object("show_list_button")
hijri_entry = builder.get_object("hijri_entry")
gregorian_entry = builder.get_object("gregorian_entry")
convert_button.grab_focus()

window.connect("destroy", Gtk.main_quit)
window.show_all()

hijri_combo_box.hide()
hijri_year_entry.hide()
gregorian_combo_box.hide()
gregorian_year_entry.hide()
show_list_button.set_sensitive(False)
hijri_entry.set_tooltip_markup("Set Hijri Year")
gregorian_entry.set_tooltip_markup("Set Gregorian Year")

Gtk.main()
