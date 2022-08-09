# DataBase Indexes comparison

To run the app just type this command in your terminal.

```
make up
```
# Results

| Requests                                                                                                     |            default |      btree |       hash |
| :----------------------------------------------------------------------------------------------------------- | -----------------: | ---------: | ---------: |
| SELECT SQL*NO_CACHE count(\*) FROM users_indexes WHERE created_date*? = '2013-01-23';                        | longer than 10 min |   0.003453 |   0.006234 |
| SELECT SQL*NO_CACHE count(\*) FROM users_indexes WHERE created_date*? > '2013-01-23';                        |  longer than 10min | 303.299789 | 370.753075 |
| SELECT SQL*NO_CACHE count(\*) FROM users_indexes WHERE created_date*? <> '2013-01-23' LIMIT 100000;          | longer than 10 min |   5.137924 |   1.539777 |
| SELECT SQL*NO_CACHE count(\*) FROM users_indexes WHERE created_date*? BETWEEN '2013-01-23' AND '2018-01-23'; |   more than 20 min |     21 sec |    208 sec |

- Hash index fast working with =. <> operations but not with ranges.
- BTree index works like log(N) to find the value in the key.

> Where 0, 1, 2 is innodb_flush_log_at_trx_commit

| Operations                                    | 0         | 1         | 2         |
|     :---:      |     :---:      |     :---:      |     :---:      |
| 1                                             | 1.05 secs | 1.12 secs | 1.11 secs |
| 5                                             | 1.24 secs | 1.94 secs | 1.23 secs |
| 50                                            | 2.56 secs | 5.32 secs | 2.43 secs |
| 100                                           | 3.17 secs | 5.16 secs | 3.51 secs |
