SELECT rewardsReceiptStatus, SUM(purchasedItemCount), AVG(totalSpent)
FROM receiptscopy
WHERE rewardsReceiptStatus = "FINISHED" OR rewardsReceiptStatus = 'REJECTED'
GROUP BY rewardsReceiptStatus
ORDER BY rewardsReceiptStatus;

/*
Note: In the JSON/CSV file, there is no records with rewards status named "Accepted."
However, there are rows with status named "Finished." Hence, if one wants to run this script
against the given data, then "ACCEPTED" should be replaced by "FINISHED"
*/