import io

from common import database
from .db import DBSwitch, use_open_dbsession, DBgearrequest, DBPropertyifo, DBCables
from datetime import datetime
import logging
from .settings import people, ethernetcable

#excel module
import xlsxwriter

class gearrequest:
    def __int__(self):
        pass

####################### table modifiers #########################
    def add_request_gear(self,unid,config_data):
        """
        Add a gear request to the gearrequest database.

        Args:
            dbid (str): Ipaddress.
            config_data (dic): A dictionary of data from handler

        Raises:
            ValueError: Caused if dbid is not provided.
        """
        if not config_data['management_ip']:
            raise ValueError("No IPaddress given")

        with database.db_session() as dbsession:
            gearexisting = dbsession.query(DBgearrequest).filter(
                    DBgearrequest.ip == config_data['management_ip']).first()
            if not gearexisting:
                dbsession.add(DBgearrequest(gearrequestdate=datetime.now().strftime("%m/%d/%Y"),
                                            unid=unid,
                                            ip=config_data['management_ip'],
                                            Hostname=config_data['hostname'],
                                            pickupdate=config_data['pickup date']))
                dbsession.commit()
                gearexisting = dbsession.query(DBgearrequest).filter(
                    DBgearrequest.ip == config_data['management_ip']).first()
                if not gearexisting:
                    raise ValueError("Database entry not added")
                else:
                    return gearexisting.id
            else:
                raise LookupError(f"Entry Already Exists:{gearexisting.id}")

    def delete_request_gear(self, tableid):
        """
        Deletes a row from the table gearrequest

        Args:
            dbid (str): Ipaddress.
            uid (str): the ID of the User submitting the gear request
            hostname (str): Hostname pulled from the switch, not dns.

        Raises:
            ValueError: Caused if the entry can be found in the table after delete
            KeyError: Caused if unable to locate entry for deleting
        """
        with database.db_session() as dbsession:
            gearexisting = dbsession.query(DBgearrequest).filter(
                    DBgearrequest.id == tableid).delete(synchronize_session=False)
            if gearexisting:
                gearexisting = dbsession.query(DBgearrequest).filter(
                    DBgearrequest.id == tableid).first()
                if not gearexisting:
                    return "Deleted Succesfully"
                else:
                    raise ValueError("Database entry not deleted")
            else:
                raise KeyError("Unable to find entry")

    def delete_property(self,tableid):
        """
        Add a gear request to the gearrequest database.

        Args:
            dbid (int): the id of the row to be deleted

        Raises:
            ValueError: Caused if the entry can be found in the table after delete
            KeyError: Caused if unable to locate entry for deleting
        """
        with database.db_session() as dbsession:
            Property = dbsession.query(DBPropertyifo).filter(
                    DBPropertyifo.id == tableid).delete(synchronize_session=False)
            if Property:
                Property = dbsession.query(DBPropertyifo).filter(
                    DBPropertyifo.id == tableid).first()
                if not Property:
                    return "Deleted Succesfully"
                else:
                    raise ValueError("Database entry not deleted")
            else:
                raise KeyError("Unable to find entry")
    def delete_ebc(self,tableid):
        """
        Add a gear request to the gearrequest database.

        Args:
            dbid (int): the id of the row to be deleted

        Raises:
            ValueError: Caused if the entry can be found in the table after delete
            KeyError: Caused if unable to locate entry for deleting
        """
        try:
            with database.db_session() as dbsession:
                Property = dbsession.query(DBCables).filter(
                        DBCables.id == tableid).delete(synchronize_session=False)
                dbsession.commit()
                if Property:
                    Property = dbsession.query(DBCables).filter(
                        DBCables.id == tableid).first()
                    if not Property:
                        return "Deleted Succesfully"
                    else:
                        raise ValueError("Database entry not deleted")
                else:
                    return "Deleted Succesfully"
        except Exception as e:
            logging.error(e, exc_info=True)
            raise ValueError("Database entry not deleted")

    # def _add_new_location(self,room,bldg):
    #     with database.db_session() as dbsession:
    #         previous_location = dbsession.query(DBLocation).filter(
    #             DBLocation.room == room, DBLocation.building_number == bldg).first()
    #         if not previous_location:
    #             dbsession.add(DBLocation(room=room,
    #                                     building_number=bldg))
    #             dbsession.commit()
    #             current_location = dbsession.query(DBLocation).filter(
    #                 DBLocation.room == room, DBLocation.building_number == bldg).first()
    #             if not current_location:
    #                 raise ValueError("Database entry not added")
    #             else:
    #                 return current_location.id
    #         else:
    #             return ("Previous Entry", previous_location.id)

    def add_request_property(self, ddc_id, geartype, make, model, mac, room, building, quantity,
                             itemnumber=None, description=None, tableidlist=None):
        """

        Args:
            ddc_id (int):
            geartype (str):
            make (str):
            model (str):
            mac (str):
            room (str):
            building (str):
            quantity (str):
            tableidlist (list): An optional id that will cause the search to ignore that value

        Returns:

        Raises:

        """
        try:
            propertyexisting = None
            with database.db_session() as dbsession:
                if not tableidlist:
                    propertyexisting = dbsession.query(DBPropertyifo).filter(
                        DBPropertyifo.ddc_id == ddc_id,
                        DBPropertyifo.geartype == geartype,
                        DBPropertyifo.make == make,
                        DBPropertyifo.model == model,
                        DBPropertyifo.model == description,
                        DBPropertyifo.quantity == quantity,
                        DBPropertyifo.itemnumber == itemnumber,
                        DBPropertyifo.mac == mac,
                        DBPropertyifo.roomnumber == room,
                        DBPropertyifo.buildingnumber == building).all()

                if propertyexisting:
                    if tableidlist:
                        for row in propertyexisting:
                            for value in tableidlist:
                                if value == row.id:
                                    return "Entry Exists"
                                else:
                                    continue
                dbsession.add(DBPropertyifo(ddc_id= ddc_id,
                                            geartype= geartype,
                                            make= make,
                                            model= model,
                                            quantity= int(quantity),
                                            description=description,
                                            itemnumber=itemnumber,
                                            mac= mac,
                                            roomnumber= room,
                                            buildingnumber= building))
                dbsession.commit()
                propertyexisting = dbsession.query(DBPropertyifo).filter(
                    DBPropertyifo.ddc_id==ddc_id,
                    DBPropertyifo.geartype==geartype).all()

                if not propertyexisting:
                    raise LookupError("Database Entry for Property not created")
                else:
                    if tableidlist:
                        for value in tableidlist:
                            for row in propertyexisting:
                                if value == row.id:
                                    continue
                                else:
                                    return row.id
                    else:
                        return propertyexisting[0].id
        except Exception as e:
            logging.error(e, exc_info=True)


    def add_request_ebc(self, tableid, partnumber,quantity,mac,tableidlist=None):
        """
        For adding the initial orders to the ebc warehouse database
        the EBC warehouse only handles requests for fiber cables.
        Args:
            tableid (int): The table number of Gearrequest
            config_data (dic): The dictionary from webpage

        Raises:
            ValueError: Caused if dbid is not provided.
            LookupError: If the Entry was not added to the database
        """
        try:
            if not tableid:
                raise ValueError("No gearrequest.id given")

            with database.db_session() as dbsession:
                cableexisting = dbsession.query(DBCables).filter(
                    DBCables.ebc_id == tableid,
                    DBCables.fiberquantity == quantity,
                    DBCables.fibermac == mac,
                    DBCables.fiberpartnumber == partnumber).all()

                if cableexisting:
                    if tableidlist:
                        for row in cableexisting:
                            for value in tableidlist:
                                if value == row.id:
                                    return "Entry Exists"
                                else:
                                    continue
                dbsession.add(DBCables(ebc_id= tableid,
                                       fiberquantity= quantity,
                                       fibermac= mac,
                                       fiberpartnumber= partnumber))
                dbsession.commit()
                cableexisting = dbsession.query(DBCables).filter(
                    DBCables.ebc_id == tableid,
                    DBCables.fiberquantity == quantity,
                    DBCables.fibermac == mac,
                    DBCables.fiberpartnumber == partnumber).all()
                if not cableexisting:
                    raise LookupError("Database Entry for Property not created")
                else:
                    if tableidlist:
                        for value in tableidlist:
                            for row in cableexisting:
                                if value == row.id:
                                    continue
                                else:
                                    return row.id
                    else:
                        return cableexisting[0].id
        except Exception as e:
            logging.error(e, exc_info=True)
        else:
            return "Succesffuly added"

    def get_all_orders(self):
        dblist = []
        with database.db_session() as dbsession:
            gearexisting = dbsession.query(DBgearrequest).filter(
                DBgearrequest.gearinstalldate == None)
            if gearexisting:
                for request in gearexisting.all():
                    requestdb = {}
                    requestdb[f"id"] = request.id
                    requestdb[f"ip"] = request.ip
                    requestdb[f"hostname"] = request.Hostname
                    requestdb[f"unid"] = request.unid
                    requestdb[f"pickupdate"] = request.pickupdate
                    requestdb[f"name"] = people[request.unid]
                    propertyexisting = dbsession.query(DBPropertyifo).filter(
                        DBPropertyifo.ddc_id == request.id)
                    if propertyexisting:
                        items = []
                        for item in propertyexisting.all():
                            items.append(dict(item.__dict__))
                        requestdb["ddc_items"] = items
                    cablesexisting = dbsession.query(DBCables).filter(
                        DBCables.ebc_id == request.id)
                    if cablesexisting:
                        items = []
                        for item in cablesexisting.all():
                            logging.info(dict(item.__dict__))
                            items.append(dict(item.__dict__))
                        requestdb["ebc_items"] = items
                    dblist.append(requestdb)
                return dblist
            else:
                raise LookupError("No Entries exist")

    def get_list_all_orders(self):
        dblist = []
        with database.db_session() as dbsession:
            gearexisting = dbsession.query(DBgearrequest).filter(
                DBgearrequest.gearinstalldate == None)
            if gearexisting:
                for request in gearexisting.all():
                    requestdb = {}
                    requestdb[f"id"] = request.id
                    requestdb[f"ip"] = request.ip
                    requestdb[f"hostname"] = request.Hostname
                    requestdb[f"unid"] = request.unid
                    requestdb[f"pickupdate"] = request.pickupdate
                    requestdb[f"name"] = people[request.unid]
                return dblist
            else:
                raise LookupError("No Entries exist")

    def get_gearrequests(self, tableid=None, ip=None, unid=None, hostname=None):
        """

        Args:
            dbid (str): Ipaddress.
            uid (str): the ID of the User submitting the gear request
            hostname (str): Hostname pulled from the switch, not dns.

        Raises:
            LookupError: Caused if not able to find the entry
            KeyError: Caused if IP, unid, and hostname are not filled out completely

        Returns:
            List: A list of dictionaries
        """
        dblist = []
        with database.db_session() as dbsession:
            if tableid:
                gearexisting = dbsession.query(DBgearrequest).filter(
                    DBgearrequest.id == tableid)
            elif ip and unid and hostname:
                gearexisting = dbsession.query(DBgearrequest).filter(
                    DBgearrequest.ip == ip,
                    DBgearrequest.unid == unid,
                    DBgearrequest.Hostname == hostname)
            else:
                raise KeyError("Not enough Values to find entry")
            if gearexisting:
                for request in gearexisting.all():
                    dblist.append(dict(request.__dict__))
                return dblist
            else:
                raise LookupError("No Entries exist")

    def get_property(self, tableid=None):
        """

        Args:
            dbid (str): Ipaddress.
            uid (str): the ID of the User submitting the gear request
            hostname (str): Hostname pulled from the switch, not dns.

        Raises:
            LookupError: Caused if not able to find the entry
            KeyError: Caused if IP, unid, and hostname are not filled out completely

        Returns:
            List: A list of dictionaries
        """
        dblist = []
        with database.db_session() as dbsession:
            if tableid:
                Property = dbsession.query(DBPropertyifo).filter(
                    DBPropertyifo.ddc_id == tableid)
            else:
                raise KeyError("Not enough Values to find entry")
            if Property:
                for request in Property.all():
                    dblist.append(dict(request.__dict__))
                return dblist
            else:
                raise LookupError("No Entries exist")

    def get_ebc(self, tableid=None):
        """

        Args:
            dbid (int): gearrequest.id

        Raises:
            LookupError: Caused if not able to find the entry
            KeyError: Caused if IP, unid, and hostname are not filled out completely

        Returns:
            List: A list of dictionaries
        """
        dblist = []
        with database.db_session() as dbsession:
            if tableid:
                Property = dbsession.query(DBCables).filter(
                    DBCables.ebc_id == tableid)
            else:
                raise KeyError("Not enough Values to find entry")
            if Property:
                for request in Property.all():
                    dblist.append(dict(request.__dict__))
                return dblist
            else:
                raise LookupError("No Entries exist")

    def update_request_gear(self, id, date):
        """
        Add a gear request to the gearrequest database.

        Args:
            dbid (str): Ipaddress.
            uid (str): the ID of the User submitting the gear request
            hostname (str): Hostname pulled from the switch, not dns.

        Raises:
            ValueError: Caused if dbid is not provided.

        Returns:
            gearexisting (str): gearrequest.id
        """
        with database.db_session() as dbsession:
            gearexisting = dbsession.query(DBgearrequest).filter(
                    DBgearrequest.id == id).first()
            if gearexisting:
                gearexisting.ordercompletedate=date
                dbsession.commit()
                gearexisting = dbsession.query(DBgearrequest).filter(
                    DBgearrequest.id == id).first()
                if not gearexisting.ordercompletedate:
                    raise KeyError("Record not updated")
                else:
                    return gearrequest
            else:
                raise LookupError("No Record Found")

    def update_request_property(self, id, gearrequestid, geardict, date):
        """
        Add a gear request to the gearrequest database.

        Args:
            dbid (str): Ipaddress.
            uid (str): the ID of the User submitting the gear request
            hostname (str): Hostname pulled from the switch, not dns.

        Raises:
            ValueError: Caused if dbid is not provided.

        Returns:
            gearexisting (str): gearrequest.id
        """
        logging.info(geardict)
        with database.db_session() as dbsession:
            propertyexisting = dbsession.query(DBPropertyifo).filter(
                DBPropertyifo.id == id,
                DBPropertyifo.ddc_id == gearrequestid).first()
            if propertyexisting:
                propertyexisting.barcode = geardict['uittag']
                propertyexisting.propertytag=geardict['assesttag']
                propertyexisting.assettagcolor=geardict['kindoftag']
                propertyexisting.serialnumber=geardict['serial']
                propertyexisting.make=geardict['make']
                propertyexisting.model=geardict['model']
                propertyexisting.quantity=geardict['quantity']
                propertyexisting.itemnumber=geardict['itemnumber']
                propertyexisting.description=geardict['description']
                propertyexisting.roomnumber=geardict['room']
                propertyexisting.buildingnumber=geardict['building']
                propertyexisting.temptag=geardict['temptag']
                propertyexisting.ordercompletedate = date
                dbsession.commit()
                propertyexisting = dbsession.query(DBPropertyifo).filter(
                    DBPropertyifo.id == id).first()
                if not propertyexisting.ordercompletedate and not propertyexisting.serialnumber:
                    raise KeyError("Record not updated")
                else:
                    return propertyexisting
            else:
                raise LookupError("No Record Found")

    def update_ebc(self, id, gearrequestid, geardict, date):
        """
        Add a gear request to the gearrequest database.

        Args:
            dbid (str): Ipaddress.
            uid (str): the ID of the User submitting the gear request
            hostname (str): Hostname pulled from the switch, not dns.

        Raises:
            ValueError: Caused if dbid is not provided.

        Returns:
            gearexisting (str): gearrequest.id
        """
        logging.info(geardict)
        with database.db_session() as dbsession:
            cableexisting = dbsession.query(DBCables).filter(
                DBCables.id == id).first()
            if cableexisting:
                cableexisting.fiberordercompletedate = geardict['uittag']
                cableexisting.fiberpartnumber=geardict['assesttag']
                cableexisting.fiberquantity=geardict['kindoftag']
                cableexisting.fibermac = geardict['kindoftag']

                dbsession.commit()
                cableexisting = dbsession.query(DBCables).filter(
                    DBCables.id == id).first()
                if not cableexisting.fiberordercompletedate:
                    raise KeyError("Record not updated")
                else:
                    return cableexisting
            else:
                raise LookupError("No Record Found")

    def create_excel(self, geardict,uid, IO=False):
        """
        Generates the Excel spreadsheet for Inventory
        Returns ():
        """
        date = datetime.now()
        output = None
        try:
            if IO:
                output = io.BytesIO()
                workbook = xlsxwriter.Workbook(output, {'in_memory': True})
            else:
                filename = "_".join(geardict['requestor'].split(" ")) + '_' + date.strftime("%m_%d_%Y%_%H_%M_%S") + ".xlsx"
                workbook = xlsxwriter.Workbook(filename)
            workbook = self._create_excel_template(workbook)
            # Write some test data.
            worksheet = workbook.get_worksheet_by_name('Warehouse Checkout&Return Form')
            title_1_size_box_top_left = workbook.add_format({'font_size': 14, 'bold': True,
                                                             'font_name': 'Calibri', 'bottom': 1,
                                                             'top': 1, 'left': 1,
                                                             'right': 1, 'align': 'left',
                                                             'valign': 'top', 'text_wrap': True})
            worksheet.merge_range('F36:H37', f"NAME (PLEASE PRINT)\n{geardict['requestor']}", title_1_size_box_top_left)
            worksheet.merge_range('F32:H33', f"NAME (PLEASE PRINT)\n{people[uid]}", title_1_size_box_top_left)
            # rows
            row = 11
            for key, value in geardict['ddc_rows'].items():
                worksheet.write(f'A{row}', f"{value['itemnumber']}")
                worksheet.write(f'B{row}', f"{value['uittag']}")
                worksheet.write(f'C{row}', f"{value['temptag']}")
                worksheet.write(f'D{row}', f"{value['assesttag']}")
                worksheet.write(f'E{row}', f"{value['kindoftag']}")
                worksheet.write(f'F{row}', f"{value['description']}")
                worksheet.write(f'G{row}', f"{value['make']}")
                worksheet.write(f'H{row}', f"{value['model']}")
                worksheet.write(f'I{row}', f"{value['serial']}")
                worksheet.write(f'J{row}', f"{value['quantity']}")
                worksheet.write(f'K{row}', f"Bldg:{value['building']} Room:{value['room']}")
                worksheet.write(f'L{row}', f"{value['mac']}")
                row = row + 1
            # Close the workbook before streaming the data.
            workbook.close()
        except Exception as e:
            logging.error(e,exc_info=True)
        else:
            if IO:
                output.seek(0)
                return output
            else:
                return workbook

    def _create_excel_template(self, workbook):
        """
        Create the Switch checkout form as a template, and formmating properly
        Args:
            workbook ():
        Returns:
        """
        try:
            worksheet = workbook.add_worksheet('Warehouse Checkout&Return Form')
            # Add a bold format to use to highlight cells.
            title_1_size = workbook.add_format({'font_size': 14, 'bold': True, 'font_name': 'Calibri'})
            title_1_size_box_top_left = workbook.add_format({'font_size': 14,
                                                             'bold': True,
                                                             'font_name': 'Calibri',
                                                             'bottom': 1,
                                                             'top':1,
                                                             'left':1,
                                                             'right':1,
                                                             'align':'left',
                                                             'valign':'top'})
            title_1_size_box_top_left_bulk = workbook.add_format({'font_size': 11,
                                                             'font_name': 'Calibri',
                                                             'align': 'left',
                                                             'valign': 'top',
                                                            'text_wrap': True})
            title_2_size = workbook.add_format({'font_size': 20, 'bold': True, 'font_name': 'Calibri'})
            title_3_size = workbook.add_format({'font_size': 12, 'bold': True, 'font_name': 'Calibri'})
            form_1_underline = workbook.add_format({'font_size': 12, 'bold': True, 'font_name': 'Calibri', 'bottom':1})
            box = workbook.add_format({'font_size': 12, 'font_name': 'Calibri',
                                       'bottom': 1, 'top':1, 'left':1, 'right':1,
                                       'bg_color':'#808080', 'text_wrap': True,
                                       'align':'center','valign':'top'}
                                      )
            box_nogray = workbook.add_format({'font_size': 12, 'font_name': 'Calibri',
                                       'bottom': 1, 'top': 1, 'left': 1, 'right': 1})
            thickbox = workbook.add_format(
                {'font_size': 12, 'font_name': 'Calibri', 'bottom': 2, 'top': 2, 'left': 2, 'right': 2,
                 'align':'Left','valign':'top','bold': True,'text_wrap': True})
            thickbox_nobottom = workbook.add_format(
                {'font_size': 12, 'font_name': 'Calibri', 'top': 2, 'left': 2, 'right': 2,'bg_color':'#808080',
                 'align':'center','valign':'top'})
            thickbox_bottom = workbook.add_format(
                {'font_size': 12, 'font_name': 'Calibri', 'bottom':1,'top': 1, 'left': 2, 'right': 2})
            title_3_size_gray = workbook.add_format({'font_size': 12, 'bold': True, 'font_name': 'Calibri',
                                                'bg_color':'#808080','align':'center','valign':'top'})

            # create Worksheet template
            worksheet.merge_range('B1:C1', "UIT WAREHOUSE",title_1_size)
            worksheet.merge_range('B2:F2', "CHECKOUT / RETURN FORM",title_2_size)
            worksheet.merge_range('B4:E4', "IS THIS TO BE BILLED TO ANOTHER DEPARRTMENT?",title_3_size)
            worksheet.write('F4', "No", title_1_size)
            worksheet.merge_range('B5:C5', "DEPARTMENT NAME:", title_3_size)
            worksheet.merge_range('D5:E5', "UIT NOC",form_1_underline)
            worksheet.merge_range('F5:G5', "DEPARTMENT CONTACT:", title_3_size)
            worksheet.merge_range('H5:I5', "Ray Carsey", form_1_underline)
            worksheet.merge_range('D6:H6', "**ANY ITEM WITH A SERIAL NUMBER MUST BE LISTED INDIVIDUALLY**", title_3_size)
            worksheet.merge_range('K1:K2', f"Date: \n {datetime.now().strftime('%m/%d/%Y')}", thickbox)
            worksheet.write('K4', f"Mark one below:", title_3_size)
            worksheet.merge_range('K5:K6', f"X Checkout", thickbox)
            worksheet.merge_range('A9:A10', f"ITEM #", box)
            worksheet.set_column('B:B', 11)
            worksheet.merge_range('B9:B10', f"UIT TAG # \r\n (Silver)", box)
            worksheet.set_column('C:C', 11)
            worksheet.merge_range('C9:C10', f"Temp. Tag#", box)
            worksheet.set_column('D:D', 11)
            worksheet.merge_range('D9:D10', f"ASSET TAG #", box)
            worksheet.set_column('E:E', 14)
            worksheet.merge_range('E9:E10', f"KIND OF TAG \r\n (Red or Yellow)", box)
            worksheet.merge_range('F9:I9', f"PRODUCT DESCRIPTION", thickbox_nobottom)
            worksheet.set_column('F:F', 20)
            worksheet.write('F10', f"DESCRIPTION", box)
            worksheet.set_column('G:G', 11)
            worksheet.write('G10', f"MAKE", box)
            worksheet.set_column('H:H', 15)
            worksheet.write('H10', f"MODEL", box)
            worksheet.set_column('I:I', 15)
            worksheet.write('I10', f"SERIAL", box)
            worksheet.set_column('J:J', 5)
            worksheet.merge_range('J9:J10', f"QTY", box)
            worksheet.set_column('K:K', 25)
            worksheet.merge_range('K9:K10', f"JOB NAME OR DEPLOYMENT\r\nLOCATION", box)
            worksheet.set_column('L:L', 11)
            worksheet.merge_range('L9:L10', f"PO #   and/or\r\nMAC #", box)

            worksheet.merge_range('B31:D31', f"WAREHOUSE STAFF", title_1_size)
            worksheet.set_row(32, 30)
            worksheet.set_row(33, 30)
            worksheet.merge_range('B32:E33', f"AUTHORIZED SIGNATURE", title_1_size_box_top_left)
            worksheet.merge_range('B35:D35', f"UIT TECHNICIAN", title_1_size)
            worksheet.set_row(36, 30)
            worksheet.set_row(37, 30)
            worksheet.merge_range('B36:E37', f"AUTHORIZED SIGNATURE", title_1_size_box_top_left)
            worksheet.merge_range('B38:D38', f"CONTRACTOR NAME", title_1_size)
            worksheet.set_row(39, 30)
            worksheet.merge_range('B39:H39', "", box_nogray)
            worksheet.merge_range('B40:D40', f"CONTRACTOR SIGNATURE ", title_1_size)
            worksheet.set_row(41, 30)
            worksheet.set_row(42, 30)
            worksheet.merge_range('B41:E42', f"AUTHORIZED SIGNATURE", title_1_size_box_top_left)
            worksheet.merge_range('F41:H42', f"NAME (PLEASE PRINT)", title_1_size_box_top_left)
            worksheet.merge_range('I32:L42', """BY SIGNING THIS FORM I ACKNOWLEDGE:
-  I HAVE RECEIVED THE LISTED RED OR YELLOW TAG STICKERS 
-  I AM FULLY RESPONSIBLE FOR THE PROPER HANDLING OF THE RED OR YELLOW TAGS
-  I WILL ATTACH THE RED OR YELLOW TAG STICKERS TO THE SPECIFIED EQUIPMENT
-  I WILL PROVIDE TO ELAINE GALLEGOS ANY REQUESTED INFORMATION ABOUT THE ASSET
-- SUCH AS SERIAL #, LOCATION, ETC
-  THIS WILL BE COMPLETED WITHIN 1 WEEK OF DATE RECEIVED""", title_1_size_box_top_left_bulk)
        except Exception as e:
            logging.error(e,exc_info=True)
            raise
        else:
            return workbook

    def add_gear_request_from_handler(self,config_data,uid):
        """
        Handles creating the Database entries from RequestGear handler
        Args:
            config_data (dict): A Dictionary containing all the information for the request
        """
        tableid = self.add_request_gear(uid,config_data)
        room = config_data.get('room')
        bldg = config_data.get('bldg')
        poc = config_data.get('accesspoc')
        model = config_data.get('switch_model')
        quantity = config_data.get('switch_number')
        coppercables = config_data.get('copper cables')
        cablemanagers = config_data.get('cable manager')
        fibercables = config_data.get('fiber cables')
        power_outlets = config_data.get("power_outlets")
        rack_info = config_data.get("rack_info")

        # if room and bldg:
        #     locationid = self._add_location(room,bldg,POC)
        # for Ethernet Cable Requests
        if coppercables:
            coppercablesids = self._add_copper_cables(coppercables)

        # for Fiber Cable Requests
        if fibercables:
            fiberids = self._add_fiber_cables(fibercables)

        # add Cablemanagers to database
        if cablemanagers:
            cablemangerids = self._add_cable_managers(cablemanagers)
        if power_outlets:
            power_outletsids = self._add_power_outlets(power_outlets)

        #add switch to table
        tableids = self._add_switch(quantity)

    def _add_copper_cables(self,coppercables):
        """

        Args:
            coppercables:

        Returns:

        """
        if coppercables:
            coppercableids = []
            for ft, cable in coppercables.items():
                if ft:
                    logging.info(f"coppercable:{cable}")
                    result = self.add_request_property(ddc_id=tableid,
                                           geartype="Patch Cable",
                                           make="Clearlinks",
                                           model="Cat 6",
                                           mac="UIT Mac",
                                            itemnumber=ft,
                                            description=ethernetcable[ft],
                                           building=bldg,
                                           room=room,
                                           quantity=cable)
                    coppercableids.append(result)
            return coppercableids

    def _add_fiber_cables(self,fibercables):
        """

        Args:
            fibercables:

        Returns:

        """
        fiberids = []
        for ft, cable in fibercables.items():
            if ft:
                logging.info(f"fibercable:{cable}")
                result = self.add_request_ebc(tableid=tableid, partnumber=ft, quantity=cable,
                                              mac="UIT MAC", tableidlist=fiberids)
                fiberids.append(result)
        return fiberids

    def _add_cable_managers(self,cablemanagers):
        """

        Args:
            cablemanagers:

        Returns:

        """
        cablemangerids = []
        for size, qunantity in cablemanagers.items():
            description = None
            if size:
                if size == 'WM1455':
                    description = "2-U Cable Manager"
                elif size == 'WM1435':
                    description = "1-U Cable Manager"
                result = self.add_request_property(ddc_id=tableid,
                                                   geartype="Cable Manager",
                                                   make="Unknown",
                                                   model="Unknown",
                                                   description=description,
                                                   mac="UIT Mac",
                                                   itemnumber=size,
                                                   building=bldg,
                                                   room=room,
                                                   quantity=qunantity)
                cablemangerids.append(result)
        return cablemangerids

    def _add_switch(self,quantity):
        """

        Args:
            quantity:

        Returns:

        """
        tableids = []
        for i in range(0, int(quantity)):
            # addding switch
            result = self.add_request_property(ddc_id=tableid,
                                            geartype="Switch",
                                            make="Cisco",
                                            model=model,
                                            mac="UIT Mac",
                                            building=bldg,
                                            room=room,
                                            quantity="1",
                                            tableidlist=tableids)
            tableids.append(result)
            if result == "Entry Exists":
                logging.info("Entry Exists")
            else:
                logging.info("switch added")
        return tableids

    def _add_power_outlets(self,power_outlets):
        """

        Args:
            power_outlets:

        Returns:

        """
        power_outletsids = []
        for outlet_name, outletlist in power_outlets.items():
            amps = outletlist[0]
            volts = outletlist[1]
            result = self.add_request_ebc(tableid=tableid, partnumber=ft, quantity=cable,
                                          mac="UIT MAC", tableidlist=power_outletsids)
            power_outletsids.append(result)
        return power_outletsids

    def _add_location(self,room,bldg,poc):
        """
        adds room, and buildings information to out locations database
        Args:
            room:
            bldg:
        Returns:
        """
        locationid = None
        amps = outletlist[0]
        volts = outletlist[1]
        message, resultid = self.add_request_ebc(tableid=tableid, partnumber=ft, quantity=cable,
                                      mac="UIT MAC", tableidlist=power_outletsids)
        if message == "Previous Entry": # need to update the entry
            pass
        else:
            locationid = resultid
        return locationid

    def update_database_from_handler(self,gear_data,uid):
        """
        Args:
            gear_data (dict): A Dictionary of the completed order
            uid (str): the uid of the warehouse worker making order complete

        Returns:
        """
        date = datetime.now().strftime('%m/%d/%Y')
        self.update_request_gear(gear_data['gearrequeastid'], date=date)
        if "ddc_rows" in gear_data.keys():
            for id, row in gear_data['ddc_rows'].items():
                self.update_request_property(id, gear_data['gearrequeastid'], row, date)
        elif "ebc_rows" in gear_data.keys():
            for row in gear_data['ebc_rows'].items():
                self.update_ebc(gear_data['gearrequeastid'], date=date)
        excelfile = self.create_excel(gear_data,uid, IO=True)
        return excelfile