using System;
using System.IO;
using System.Windows.Forms;
using SevenZip;

namespace ARCed.Helpers
{
	public static class Compressor
	{

		private static SevenZipCompressor _compressor;
		private static SevenZipExtractor _extractor;
		private static bool _notify;

		/// <summary>
		/// Compresses a directory into a single archive
		/// </summary>
		/// <param name="inDir">The path to the directory to compress</param>
		/// <param name="outFile">The archive name to create</param>
		/// <param name="notify">Flag to notify user when finished</param>
		public static void CompressDirectory(string inDir, string outFile, bool notify = false)
		{
			SevenZip.SevenZipBase.SetLibraryPath(PathHelper.SevenZip_Library);
			if (_compressor == null)
			{
				_compressor = new SevenZipCompressor();
				_compressor.ArchiveFormat = OutArchiveFormat.SevenZip;
				_compressor.CompressionLevel = CompressionLevel.Ultra;
				_compressor.CompressionMode = CompressionMode.Create;
			}
			_notify = notify;
			string tempPath = Path.GetTempPath();
			_compressor.TempFolderPath = Path.GetTempPath();
			_compressor.CompressDirectory(inDir, outFile);
			File.SetCreationTime(outFile, DateTime.Now);
		}

		/// <summary>
		/// Extracts and archive to the given directory
		/// </summary>
		/// <param name="inFile">Path to the archive to extract</param>
		/// <param name="outDir">The path to the target directory for extraction</param>
		public static void ExtractArchive(string inFile, string outDir)
		{
			SevenZip.SevenZipBase.SetLibraryPath(PathHelper.SevenZip_Library);
			try
			{
				_extractor = new SevenZipExtractor(inFile);
				if (!Directory.Exists(outDir))
					Directory.CreateDirectory(outDir);
				Editor.ProgressBar.Value = 0;
				Editor.ProgressBar.Maximum = 100;
				Editor.ProgressBar.Visible = true;
				_extractor.ExtractionFinished += new EventHandler<EventArgs>(_extractor_ExtractionFinished);
				_extractor.Extracting += new EventHandler<ProgressEventArgs>(_extractor_Extracting);
				_extractor.BeginExtractArchive(outDir);
			}
			catch
			{
				MessageBox.Show("Failed to extract ARChive.", 
					"Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
			}
		}

		private static void _extractor_Extracting(object sender, ProgressEventArgs e)
		{
			Editor.ProgressBar.Value = e.PercentDone;
		}

		private static void _extractor_ExtractionFinished(object sender, EventArgs e)
		{
			_extractor.Dispose();
			if (_notify)
				MessageBox.Show("Extraction complete!", "Message");
			Editor.ProgressBar.Visible = false;
		}
	}
}
