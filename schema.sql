CREATE DATABASE IF NOT EXISTS `school_db`;

use school_db;

DROP TABLE IF EXISTS `students`;

CREATE TABLE `students` (
  `id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL
);

INSERT INTO `students` (`name`, `email`, `phone`) VALUES
('motech noel', 'mosesnoel02@gmail.com', '+255752541568'),
('Thiago Moses', 'moses@noel.com', '0712541669'),
('Saratex Marie', 'moses@noel.com', '0712541669'),
('Kamonyo Kiiza', 'kamonyomoses@gmail.com', '+255752541568');

