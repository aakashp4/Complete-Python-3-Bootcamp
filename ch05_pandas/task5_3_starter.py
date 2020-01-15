"""
        task 5_3_starter.py     - This task reads from the database using
                                  Pandas APIs to find the maximum baseball salary
                                  ever and the player who earned it.

                                  Your task is to determine the max salary from
                                  the salaries table found in batting.db
                                  by using Pandas idxmax() and then query the
                                  database players table manually to find who's
                                  salary this was and what year it happened.

"""
import pandas as pd
import sqlite3
df = None
df_file = './batting.db'

# Step 1. Use the 'with' control to connect to the database.  Refer to the Pandas example
#         within the student manual on how to do this.  Proper syntax uses the following structure:
#                with <connection_obj> as conn:
#                    do stuff

# Step 2. Use read_sql() twice to read from BOTH tables within the 'with' control
#         The following sql should work for both:
#                   SELECT playerid, salary, year FROM salaries
#                   SELECT playerid, firstname, lastname FROM players


# Step 3. Once you have the loaded the DataFrames, get the index for the max salary value
#         using idx_max = df['salary'].idxmax()
#         Take this resulting idx_max value, plug it back into the salary column.  It should look something like this:
#                                       max_salary = df['salary'][idx_max]

#         The values for the other two columns might look something like this:
#                                       year_for_max_salary = df['year'][idx_max]
#                                       playerid = df['playerid'][idx_max]


# Step 4. Use the playerid obtained from step 3 to find the firstname and lastname of the
#         that playerid

# Step 5. Display the player's name, salary, and year for that salary.
