# Problem: The Company
link: https://www.hackerrank.com/challenges/the-company/problem?isFullScreen=true<br>
Amber's conglomerate corporation just acquired some new companies. Each of the companies follows this hierarchy:<br>
![image](https://user-images.githubusercontent.com/111542025/233720314-59b53ab3-ccdf-47b6-acf5-7c67c92b4b8a.png)<br>
Given the table schemas below, write a query to print the company_code, founder name, total number of lead managers, total number of senior managers, total number of managers, and total number of employees. Order your output by ascending company_code.<br>

### Note:
The tables may contain duplicate records.<br>
The company_code is string, so the sorting should not be numeric. For example, if the company_codes are C_1, C_2, and C_10, then the ascending company_codes will be C_1, C_10, and C_2.

### Input Format
The following tables contain company data:

* Company: The company_code is the code of the company and founder is the founder of the company.<br>
![image](https://user-images.githubusercontent.com/111542025/233720483-0f7da985-b63c-4fe6-96b1-357976a0a246.png)

* Lead_Manager: The lead_manager_code is the code of the lead manager, and the company_code is the code of the working company.<br>
![image](https://user-images.githubusercontent.com/111542025/233720571-47300afc-96e1-4c86-b02a-9c1d60ae02ff.png)

* Senior_Manager: The senior_manager_code is the code of the senior manager, the lead_manager_code is the code of its lead manager, and the company_code is the code of the working company.<br>
![image](https://user-images.githubusercontent.com/111542025/233720616-74990702-cba2-4f38-ab11-d655d8d759e3.png)

* Manager: The manager_code is the code of the manager, the senior_manager_code is the code of its senior manager, the lead_manager_code is the code of its lead manager, and the company_code is the code of the working company.<br>
![image](https://user-images.githubusercontent.com/111542025/233720677-a15aa0f4-3f08-413c-a766-9a6b0e126f5e.png)

* Employee: The employee_code is the code of the employee, the manager_code is the code of its manager, the senior_manager_code is the code of its senior manager, the lead_manager_code is the code of its lead manager, and the company_code is the code of the working company.<br>
![image](https://user-images.githubusercontent.com/111542025/233720750-15927e3b-a7e6-45cf-b58f-34b1fb4e3c6c.png)

## Sample Output
````sql
C1 Monika 1 2 1 2
C2 Samantha 1 1 2 2
````
## Explanation

In company C1, the only lead manager is LM1. There are two senior managers, SM1 and SM2, under LM1. There is one manager, M1, under senior manager SM1. There are two employees, E1 and E2, under manager M1.<br>

In company C2, the only lead manager is LM2. There is one senior manager, SM3, under LM2. There are two managers, M2 and M3, under senior manager SM3. There is one employee, E3, under manager M2, and another employee, E4, under manager, M3.<br>

# My Solution
```sql
SELECT 
    Company.company_code, 
    Company.founder, 
    COUNT(DISTINCT Lead_Manager.lead_manager_code) AS LeadManagers,
    COUNT(DISTINCT Senior_Manager.senior_manager_code) AS SeniorManagers,
    COUNT(DISTINCT Manager.manager_code) AS Managers,
    COUNT(DISTINCT Employee.employee_code) AS Employees
    
    
FROM 
    Company 
        LEFT JOIN 
    Lead_Manager USING(company_code) 
        LEFT JOIN 
    Senior_Manager USING(company_code) 
        LEFT JOIN 
    Manager USING(company_code) 
        LEFT JOIN 
    Employee USING(company_code) 
    
GROUP BY 
    Company.company_code, 
    Company.founder 
ORDER BY 
    Company.company_code;
```
