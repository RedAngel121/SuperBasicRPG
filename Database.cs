// This is a couple of examples that should help me start the SQLite Database
// I need to have help figuring this out, no one is really giving me functional examples.
namespace SuperBasicRPG
{
    class Database
    {

        public void ConnectListAndSaveSQLCompactExample()
        {
            // Create a connection to the file datafile.sdf in the program folder
            string dbfile = new System.IO.FileInfo(System.Reflection.Assembly.GetExecutingAssembly().Location).DirectoryName + "\\datafile.sdf";
            SQLConnection connection = new SQLConnection("datasource=" + dbfile);

            // Read all rows from the table test_table into a dataset (note, the adapter automatically opens the connection)
            SQLDataAdapter adapter = new SQLDataAdapter("select * from test_table", connection);
            DataSet data = new DataSet();
            adapter.Fill(data);

            // Add a row to the test_table (assume that table consists of a text column)
            data.Tables[0].Rows.Add(new object[] { "New row added by code" });

            // Save data back to the databasefile
            adapter.Update(data);

            // Close 
            connection.Close();

//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            // This library implements the common ADO.NET abstractions for connections, commands, data readers, and so on.
            using (var connection = new SqliteConnection("Data Source=hello.db"))
            {
                connection.Open();

                var command = connection.CreateCommand();
                command.CommandText = @"SELECT name FROM user WHERE id = $id";
                command.Parameters.AddWithValue("$id", id);

                using (var reader = command.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        var name = reader.GetString(0);

                        Console.WriteLine($"Hello, {name}!");
                    }
                }
            }
        }
    }
}