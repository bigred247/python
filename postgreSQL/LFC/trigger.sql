CREATE TRIGGER send_email 
BEFORE INSERT 
ON alerts
FOR EACH ROW
  IF (datasource.NEW='LFC') and (landing_status.NEW='COMPLETED')