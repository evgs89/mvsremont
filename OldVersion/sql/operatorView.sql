CREATE VIEW `operatorView` AS
SELECT allDevices.serialNumber, allDevices.type, incidents.desiredFinishDate, problems.typicalProblem, incidents.toEngineerDate, works.work, incidents.toStockDate
FROM incidents
LEFT JOIN allDevices ON incidents.idDevice = allDevices.id
LEFT JOIN problems ON incidents.idIncident = problems.incident
LEFT JOIN works ON incidents.idIncident = works.incident