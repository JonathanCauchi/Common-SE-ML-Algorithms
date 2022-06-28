 -- Return the total brokerage fees of brokers with indeces (64,65,66) group by individual product and month

 select  ProductGroup, MONTH(bt.Date) as Month, SUM(bt.brokerage) AS brokerage
 from BlotterTrades bt
 inner join TradeCaptures tc on tc.id = bt.Matched
 inner join BrokerAlias ba on ba.alias = tc.executingFirm
 INNER JOIN brokers b on b.Id = ba.Broker_Id
 where bt.Date >= '2021-07-01' AND
 b.id IN (64,65,66) AND
 bt.Book = 3
 group by ProductGroup, MONTH(bt.Date)
 order by ProductGroup, Month asc

-- Return the top 4 brokers in terms of brokerage fees.

 Select TOP(4) b.Name as broker, SUM(bt.brokerage) AS brokerage
 from BlotterTrades bt
 inner join TradeCaptures tc on tc.id = bt.Matched
 inner join BrokerAlias ba on ba.alias = tc.executingFirm
 INNER JOIN brokers b on b.Id = ba.Broker_Id
 where bt.Date >= '2021-07-01' AND
 bt.Book = 3
 group by b.Name
 order by brokerage DESC
