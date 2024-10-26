import names
import string
import random
from faker import Faker
import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


########################################
####            FUNCTIONS           ####
########################################
def main():

    def random_datetime():
        start_date = datetime.now()
        end_date = start_date + timedelta(days=10)
        return (start_date + (end_date - start_date) * random.random()).strftime("%Y-%m-%d %H:%M:%S.000")


    def random_end_datetime(start_time_str):
        start_date = datetime.strptime(start_time_str[:-4], "%Y-%m-%d %H:%M:%S")

        years_to_add = random.randint(1, 10)
        months_to_add = random.randint(1, 12)

        new_month = start_date.month + months_to_add
        new_year = start_date.year + years_to_add

        # Handles month overflow
        if new_month > 12:
            new_year += (new_month - 1) // 12  # Full years from overflow
            new_month = (new_month - 1) % 12 + 1  # Wrap around to valid month (1-12)

        try:
            end_date = start_date.replace(year=new_year, month=new_month)
        except ValueError:
            # Handle the case where the day is out of range for the new month
            # Calculate the last valid day of the new month
            if new_month == 2: 
                last_day_of_month = 29 if (new_year % 4 == 0 and (new_year % 100 != 0 or new_year % 400 == 0)) else 28
            else:
                last_day_of_month = 31 if new_month in (1, 3, 5, 7, 8, 10, 12) else 30

            end_date = start_date.replace(year=new_year, month=new_month, day=last_day_of_month)

        return end_date.strftime("%Y-%m-%d %H:%M:%S.000")


    def name_generator(num_of_names_int):
        storage = []
        while len(storage) != num_of_names_int:
            if fake.name() not in storage:
                storage.append(fake.name())
        return storage

    def industry_name_generator(num_of_names_int):
        industry_names_list = [
            "Aerospace & Defense",
            "Automotive, Industrial & Aerospace",
            "Banking",
            "Business Intelligence Software",
            "Business Services",
            "Non Profits",
            "Computer Equipment",
            "Real Estate",
            "Consumer Products",
            "Consumer Services",
            "IT Services",
            "Education",
            "Energy, Utilities & Waste Treatment",
            "Engineering, Construction",
            "Federal",
            "Government (Defense)",
            "Healthcare",
            "High Tech",
            "Hospitals & Physicians Clinics",
            "Insurance",
            "Investment Banking",
            "Management Consulting",
            "Media & Entertainment",
            "Medical Devices",
            "Mining",
            "Oil & Gas",
            "Pharmaceuticals & Biotech",
            "Retail",
            "Security Software",
            "Software",
            "State and Local Government",
            "Telecommunications",
            "Telephony & Wireless",
            "Travel & Hospitality",
            "Utilities",
            "Wholesale"]
        return [random.choice(industry_names_list) for i in range(num_of_names_int)]

    def company_name_generator(num_of_names_int):
        company_names_list = [
            "Google",
            "Microsoft",
            "Apple",
            "Amazon",
            "Facebook",
            "HubSpot",
            "AdVenture Media",
            "BrandBoost Agency",
            "Pixel Perfect Marketing",
            "Creative Pulse Agency",
            "NextGen Promotions",
            "EchoWave Marketing",
            "BrightSpark Strategies",
            "Vivid Vision Media",
            "Skyline Advertising",
            "Quantum Reach Solutions",
            "Catalyst Marketing Group",
            "Amplify Digital Agency",
            "Innovate Marketing Partners",
            "Fusion Strategies",
            "Dynamic Engagements",
            "PulsePoint Marketing",
            "Synergy Branding Agency"
        ]
        return [random.choice(company_names_list) for i in range(num_of_names_int)]


    def opp_type_generator(num_of_names_int):
        types = [
        "Amendment",
        "Cancel",
        "Evaluation",
        "Existing Customer",
        "New Customer",
        "Rebill",
        "Renewal",
        "Return",
        "Services"]
        return [random.choice(types) for i in range(num_of_names_int)]


    def email_generator(names_list, company_name_list):
        storage = []
        for i in range(len(names_list)):
            storage.append(names_list[i].replace(" ","") + "@" + company_name_list[i].lower().replace(" ","") + ".com")
        return storage


    def sf_id_generator(num_of_ids_int, obj_name_str):
        """Choose Account, Contact, Opportunity, Lead, or User"""
        def sf_record_number_generator_str(obj_prefix_str):
            def get_random_string():
                return  ''.join(random.choice(string.ascii_letters) for i in range(3))

            def get_constant_string(obj_prefix_str):
                storage = ""
                for i in obj_prefix_str:
                    if ord(i) <= 0:
                        storage += string.ascii_letters[ord(i) + (ord(i) + len(string.ascii_letters)) + 1]
                    if ord(i) > len(string.ascii_letters):
                        storage += string.ascii_letters[ord(i) - (ord(i) - len(string.ascii_letters)) - 1]
                    elif 0 > ord(i) and ord(i) < len(string.ascii_letters):
                        storage += string.ascii_letters[ord(i)]
                    else:
                        storage += "0"

                return storage

            return get_constant_string(obj_prefix_str) + get_random_string()

        def get_sf_final_id_digits(id_str):
            def chunk_sf_id_list(id_str, num_of_parts):
                storage = []
                part_size = len(id_str) // num_of_parts
                for i in range(0, len(id_str), part_size):
                    storage.append(id_str[i:i+part_size])
                return storage

            def id_chunk_to_binary(split_id_chunk_str):
                binary_str = ""
                for reverse_id_chunk in split_id_chunk_str[::-1]:
                    if reverse_id_chunk.isdigit():
                        binary_str += "0"
                    elif reverse_id_chunk == reverse_id_chunk.upper():
                        binary_str += "1"
                    else:
                        binary_str += "0"
                    # binary_str_list.append(string.ascii_letters[int(binary_str,2)])
                return string.ascii_letters[int(binary_str,2)]

            sf_id_chunked_list = chunk_sf_id_list(id_str,3)

            return id_chunk_to_binary(sf_id_chunked_list[0]) + id_chunk_to_binary(sf_id_chunked_list[1]) + id_chunk_to_binary(sf_id_chunked_list[2])

        storage = []
        sf_obj_prefix_dict = {"account": "001",
                            "contact": "003",
                            "opportunity": "006",
                            "user": "005"}

        for i in range(num_of_ids_int):
            if i not in storage:
                obj_prefix_str = sf_obj_prefix_dict[obj_name_str.strip().lower()]
                sf_15_char_id_str = obj_prefix_str + "6T" + "0000" + sf_record_number_generator_str(obj_prefix_str)
                storage.append(sf_15_char_id_str + get_sf_final_id_digits(sf_15_char_id_str))
        return storage




    ########################################
    ####        TABLE GENERATORS        ####
    ########################################

    def generate_User_table(num_of_records):
        sf_id = sf_id_generator(num_of_records,"User")
        created_date = [random_datetime() for i in range(num_of_records)]
        # account_id = sf_id_generator(num_of_records,"Account")
        # contact_id = sf_id_generator(num_of_records,"Contact")
        full_name = name_generator(num_of_records)
        company_name = company_name_generator(num_of_records)
        email_address = email_generator(full_name, company_name)
        billing_address = [fake.address() for i in range(num_of_records)]
        billing_country = ["United States" for i in range(num_of_records)]
        country_code = ["US" for i in range(num_of_records)]
        currency_iso_code = ["USD" for i in range(num_of_records)]
        billing_lat = [fake.latitude() for i in range(num_of_records)]
        billing_lon = [fake.longitude() for i in range(num_of_records)]
        phone_number = [fake.phone_number() for i in range(num_of_records)]
        is_active = [random.randint(0,1) for i in range(num_of_records)]
    
        return pd.DataFrame({"Id":sf_id,
                        "CreatedDate":created_date,
                        #  "AccountId":account_id,
                        #  "ContactId": contact_id,
                        "Full Name":full_name,
                        "Name":company_name,
                        "Email":email_address,
                        "PhoneNumber": phone_number,
                        "IsActive":is_active,
                        "BillingAddress":billing_address,
                        "BillingCountry":billing_country,
                        "BillingCountryCode":country_code,
                        "BillingLatitude":billing_lat,
                        "BillingLongitude":billing_lon,
                        "CurrencyISOCode":currency_iso_code})


    def generate_Account_table(num_of_records):
        sf_id = sf_id_generator(num_of_records,"Account")
        created_date = [random_datetime() for i in range(num_of_records)]
        description = ["ipso lorum" for i in range(num_of_records)]
        num_of_employees = [random.randint(100,10000) for i in range(num_of_records)]
        name = company_name_generator(num_of_records)
        owner_id = sf_id = sf_id_generator(num_of_records,"User")
        billing_address = [fake.address() for i in range(num_of_records)]
        billing_city = [address.split("\n")[1].split(",")[0] for address in billing_address]
        billing_country = ["United States" for i in range(num_of_records)]
        country_code = ["US" for i in range(num_of_records)]
        billing_lat = [fake.latitude() for i in range(num_of_records)]
        billing_lon = [fake.longitude() for i in range(num_of_records)]

        return pd.DataFrame({"Id":sf_id,
                        "CreatedDate":created_date,
                        "Description":description,
                        "NumberOfEmployees": num_of_employees,
                        "Name":name,
                        "OwnerId":owner_id,
                        "BillingAddress":billing_address,
                        "BillingCity":billing_city,
                        "BillingCountry":billing_country,
                        "BillingCountryCode":country_code,
                        "BillingLatitude":billing_lat,
                        "BillingLongitude":billing_lon})


    def generate_Opportunity_table(num_of_records):
            sf_id = sf_id_generator(num_of_records,"Opportunity")
            amount = [random.randint(1000,100000) for i in range(num_of_records)]
            is_won = [random.randint(0,1) for i in range(num_of_records)]
            is_closed = [1 if is_won[i] == 0 else 0 for i in range(num_of_records)]
            stage_name = ["Closed Won" if is_won[i] == 1 else "Open" for i in range(num_of_records)]
            created_date = [random_datetime() for i in range(num_of_records)]
            closed_date = [random_end_datetime(created_date[i]) for i in range(num_of_records)]
            account_id = sf_id_generator(num_of_records,"Account")
            owner_id = sf_id_generator(num_of_records,"User")
            phone_number = [fake.phone_number() for i in range(num_of_records)]
            # name = company_name_generator(num_of_records)
            industry_name = industry_name_generator(num_of_records)
            types = opp_type_generator(num_of_records)


            return pd.DataFrame({"Id":sf_id,
                        "Amount": amount,
                        "AccountId": account_id,
                        "CreatedDate":created_date,
                        "ClosedDate":closed_date,
                        "OwnerId":owner_id,
                        "IsWon":is_won,
                        "IsClosed":is_closed,
                        "StageName": stage_name,
                        "Phone Number":phone_number,
                        #  "Name":name,
                        "Industry":industry_name,
                        "Type":types})



    ########################################
    ####          MAIN FUNCTION         ####
    ########################################

    fake = Faker()
    
    print("Downloaded all libs \n")
    
    print("Creating Users, Accounts, and Opp data now. Please stand-by \n")

    #Create Account table and generate user ids
    accounts = generate_Account_table(40)
    accounts["BillingAddress"] = accounts["BillingAddress"].str.replace("\n", " ")
    ownerids = sf_id_generator(20,"User")
    random_ownerids_pdseries = pd.Series([ownerids[random.randint(0,19)] for i in range(40)])
    accounts["OwnerId"] = random_ownerids_pdseries

    #create user table & connect to Accounts
    users = generate_User_table(20)
    users["BillingAddress"] = users["BillingAddress"].str.replace("\n", " ")
    users["Id"] = ownerids
    acc_ids = accounts[["Id","OwnerId"]].rename(columns={"Id":"AccountId"})
    users = users.merge(acc_ids, how="left", left_on='Id', right_on="OwnerId").drop("OwnerId", axis=1)


    #create opportunity table
    accountid = accounts["Id"]
    random_accoundid_pdseries = pd.Series([accountid[random.randint(0,39)] for i in range(40)])
    opp = generate_Opportunity_table(40)
    opp["RecordTypeId"] = '012840000004cb0XAE'
    opp["Pricebook2Id"] = '01s840000000ZruAAU'
    opp["AccountId"] = random_ownerids_pdseries
    opp["OwnerId"] = random_accoundid_pdseries

    print("Downloading data to the 'data' folder now \n")

    # DOWNLOAD THE DATA
    dfs = [users, accounts, opp]
    df_name = ["User", "Accounts", "Opportunity"]
    [dfs[i].to_csv(f"./data/{df_name[i]}.csv") for i in range(len(df_name)) ]

    print("Download complete! \n")

if __name__ == '__main__':
    main()
