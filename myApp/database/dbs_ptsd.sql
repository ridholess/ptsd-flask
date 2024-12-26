-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 26, 2024 at 04:45 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbs_ptsd`
--

-- --------------------------------------------------------

--
-- Table structure for table `questions`
--

CREATE TABLE `questions` (
  `id` int(11) NOT NULL,
  `text` text NOT NULL,
  `weight_disagree` int(11) NOT NULL,
  `weight_neutral` int(11) NOT NULL,
  `weight_agree` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `questions`
--

INSERT INTO `questions` (`id`, `text`, `weight_disagree`, `weight_neutral`, `weight_agree`) VALUES
(1, 'Saya mengalami kejadian traumatis, seperti ancaman kematian, cedera serius, atau kekerasan seksual.', 0, 1, 4),
(2, 'Saya memiliki ingatan yang berulang, tidak disengaja, dan mengganggu tentang suatu peristiwa traumatis.', 0, 1, 4),
(3, 'Saya menyaksikan kejadian traumatis terjadi pada orang lain.', 0, 1, 4),
(4, 'Saya mengalami mimpi buruk berulang yang berhubungan dengan suatu peristiwa traumatis.', 0, 1, 4),
(5, 'Saya mengalami paparan berulang atau ekstrem terhadap detail grafis dari suatu peristiwa traumatis.', 0, 1, 4),
(6, 'Saya bereaksi keras terhadap isyarat yang mengingatkan saya pada peristiwa traumatis.', 0, 1, 4),
(7, 'Saya mengetahui bahwa suatu peristiwa traumatis terjadi pada anggota keluarga dekat atau teman.', 0, 1, 4),
(8, 'Saya mengalami kilas balik di mana saya merasa atau bertindak seolah-olah peristiwa traumatis itu terulang kembali.', 0, 1, 4),
(9, 'Saya menghindari hal-hal yang mengingatkan saya pada peristiwa traumatis, seperti orang, tempat, aktivitas, atau kenangan.', 0, 1, 4),
(10, 'Saya punya keyakinan negatif, seperti “Tidak ada seorang pun yang bisa dipercaya,” atau “Dunia ini benar-benar berbahaya.”', 0, 1, 4),
(11, 'Saya terutama merasakan emosi negatif, seperti ngeri, marah, bersalah, atau malu.', 0, 1, 4),
(12, 'Saya merasa terpisah dari orang lain.', 0, 1, 4),
(13, 'Saya terus-menerus tidak bisa merasakan emosi positif, seperti kebahagiaan atau kepuasan.', 0, 1, 4),
(14, 'Saya mudah marah tanpa atau dengan sedikit provokasi.\r\n', 0, 1, 4),
(15, 'Saya terlibat dalam perilaku sembrono atau merusak diri sendiri.', 0, 1, 4),
(16, 'Saya sangat waspada.', 0, 1, 4),
(17, 'I have an exaggerated startle response.', 0, 1, 4),
(18, 'Saya memiliki masalah dengan konsentrasi.', 0, 1, 4),
(19, 'Saya kesulitan untuk tertidur atau tetap tertidur.', 0, 1, 4),
(20, 'A traumatic event has significantly impaired my ability to function in daily life.', 0, 1, 4);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id_user` int(11) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id_user`, `nama`, `email`, `password`) VALUES
(6, 'ren', 'ren@mail.com', 'scrypt:32768:8:1$xxUPImaX6TCiGSWq$0493152eba7c735d9b8b2978a2ad189fff98b97b5ca530b0285e354c8a3c61a383ca00f634d2d627e2f9461c513c485d179ce2fe387a143079776377dd1584d7'),
(7, 'ridholess', 'ridholess@mail.com', 'scrypt:32768:8:1$7axVYiST5wIPOxsL$26c7ddccbf07283abe173b8dbe13d2ec8a200af0252616d8994e6f82aba89966110644d337b30697b268b7e864add8b24c2e786ad59db9b24463245759e1badd'),
(8, 'aku', 'aku@mail.com', 'scrypt:32768:8:1$F6ZjhHVOu4efk2in$0c1690e9967aa5f3ea58d1dce9f7b679c1d928d99905e3439884b04154874f2fe02d97d25905d6e80eda4b7c92e7c1200a1f5c08de29e8ef179d2b738d8aef0c'),
(9, 'Gray', 'gray@gmail.co', 'scrypt:32768:8:1$PLBGGsymCcrQ6W48$2b15d9d973b99febc73c69a5f52bae9676a5045782561ad68dd9223598fdfaecfeba83bf00e0ce922fbfea56ddc27fff2e94cd4437db769d6139942494126219');

-- --------------------------------------------------------

--
-- Table structure for table `user_scores`
--

CREATE TABLE `user_scores` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `score` int(11) NOT NULL,
  `status` varchar(50) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_scores`
--

INSERT INTO `user_scores` (`id`, `user_id`, `score`, `status`, `created_at`) VALUES
(1, 8, 80, 'Gejala PTSD kuat', '2024-12-26 04:28:43'),
(2, 8, 0, 'Tidak ada gejala', '2024-12-26 04:28:51'),
(3, 8, 76, 'Gejala PTSD kuat', '2024-12-26 04:29:01'),
(4, 9, 31, 'Ada sedikit gejala PTSD', '2024-12-26 05:01:28');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `questions`
--
ALTER TABLE `questions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id_user`);

--
-- Indexes for table `user_scores`
--
ALTER TABLE `user_scores`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `questions`
--
ALTER TABLE `questions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `user_scores`
--
ALTER TABLE `user_scores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `user_scores`
--
ALTER TABLE `user_scores`
  ADD CONSTRAINT `user_scores_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id_user`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
