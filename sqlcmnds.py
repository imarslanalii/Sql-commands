# SQL Triggers 
# “Event-Condition-Action Rules”
# When event occurs, check condition; if true, do action
#   1) Move monitoring logic from apps into DBMS
#   2) Enforce constraints

# Syntax
# Create Trigger name
# Before | After | Instead of Events
# [ referencing-variables]
# [For Each Row]
# When (condition)
# action

# Events = Insert, Delete, Update on Tables or Column 

# [For Each Row] 

# Optional Means if delete query has 10 rows execution whether we want to execute the trigger 10 times on one time per query, per row trigger execution 

# CREATE TRIGGER ins_student AFTER INSERT ON user
# FOR EACH ROW
# BEGIN
# IF NEW.type = 'student' THEN
#     INSERT INTO student (`id`) VALUES (NEW.id);
# END IF;
# END;

