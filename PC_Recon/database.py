"""
Tables that are needed
    Table---endpoint
    PK  |----id
        |----serial_number
        |----os_name_fk
        |----manufacturer_fk
        |----UUID

    Table---vendor
    PK  |----id
        |----name
        |----type


    Table---software_vendor
    PK  |----id
        |----name
        |----license_type
    FK  |----os_id
    FK  |----vendor_id_fk

    Table---machine_manufacturer
    PK  |----id
        |----name
        |----target
    FK  |----vendor_id_fk

    Table---operating_system
    PK  |----id
        |----os_friendly_name
        |----os_build_num
    FK  |----os_vendor_id
        |----os_arch

This table is not to be connected to any of the systems in the list.
But in future builds, this can be used for feedback an org level stuffs.
    Table---feedback
    PK  |----id
        |----os_id_fk
        |----run_time
        |----last_error
        |----leap_year
        |----python_ver
        |----boot_time
        |----os_install_date
"""
import sqlalchemy as sqla
import tkinter



#Need to setup the data model for sqlalchemy to work with.





#The thing to keep this from running right off the bat..
if __name__ == "__main__":
    pass