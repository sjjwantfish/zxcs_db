CREATE TABLE `book_info`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `author` varchar(255) NOT NULL DEFAULT '' COMMENT '作者',
  `book_name` varchar(255) NOT NULL DEFAULT '' COMMENT '书名',
  `title` varchar(255) NOT NULL DEFAULT '' COMMENT '标题',
  `url` varchar(255) NOT NULL DEFAULT '' COMMENT '书下载url',
  `brief` text NOT NULL  COMMENT '概要',
  `kind_id` int NOT NULL DEFAULT 0 COMMENT '类id',
  `bad` int NOT NULL DEFAULT 0 COMMENT '毒草',
  `not_bad` int NOT NULL DEFAULT 0 COMMENT '枯草',
  `normal` int NOT NULL DEFAULT 0 COMMENT '干草',
  `good` int NOT NULL DEFAULT 0 COMMENT '粮草',
  `very_good` int NOT NULL COMMENT '仙草',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='书信息表';
-- TODO: 增加外键


CREATE TABLE `book_kind` (
  `id` int NOT NULL AUTO_INCREMENT,
  `kind_name` varchar(255) NOT NULL DEFAULT '' COMMENT '类名称',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='书类别表';
