CREATE TABLE `users` (
  `id` INTEGER,
  `full_name` TEXT,
  `email` TEXT,
  `created_at` TEXT,
  `role` TEXT
);

INSERT INTO `users` (`id`, `full_name`, `email`, `created_at`, `role`) VALUES (1, 'Alice', 'a@b.com', '2025-06-11', 'Student');
INSERT INTO `users` (`id`, `full_name`, `email`, `created_at`, `role`) VALUES (2, 'Bob', 'b@c.com', '2025-06-11', 'Teacher');
