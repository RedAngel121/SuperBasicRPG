// This is a bunch of examples that should help me start the SQLite Database.
using System;
using System.Data.SQLite;
namespace SuperBasicRPG
{
    class Database
    {
        public static void CreateDataBase()
        {
            if (!System.IO.File.Exists("SBRPG.ctrl"))
            {
                SQLiteConnection.CreateFile("SBRPG.ctrl");
            }
            SQLiteConnection m_dbConnection = new SQLiteConnection("Data Source=SBRPG.ctrl;Version=3;");
            m_dbConnection.Open();

            string getNamesFromDB = "SELECT name FROM character";
            SQLiteCommand command = new SQLiteCommand(getNamesFromDB, m_dbConnection);

            cmd.CommandText = "DROP TABLE IF EXISTS character";
            cmd.ExecuteNonQuery();

            cmd.CommandText = @"CREATE TABLE character(id INTEGER PRIMARY KEY, name VARCHAR(100), race VARCHAR(100))";
            cmd.ExecuteNonQuery();

            string sql = "CREATE TABLE character(id INTEGER PRIMARY KEY, name VARCHAR(100), race VARCHAR(100))";
            command  = new SQLiteCommand(sql, m_dbConnection);
            command.ExecuteNonQuery();

            cmd.CommandText = @"INSERT INTO character (name, race) VALUES ('Dr. Gerald Riximas', 'Vanaran')";
            cmd.ExecuteNonQuery();

            Console.WriteLine("Table 'character' created");

            using SQLiteDataReader rdr = cmd.ExecuteReader();

            while (rdr.Read())
            {
                Console.WriteLine($"{rdr.GetInt32(0)} {rdr.GetString(1)} {rdr.GetString(2)}");
            }
        }
        /*

//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

// This is the query which will create a new table in our database file with three columns. An auto increment column called "ID", and two NVARCHAR type columns with the names "Key" and "Value"
string createTableQuery = @"CREATE TABLE IF NOT EXISTS [MyTable] (
                          [ID] INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                          [Key] NVARCHAR(2048)  NULL,
                          [Value] VARCHAR(2048)  NULL
                          )";
 
System.Data.SQLite.SQLiteConnection.CreateFile("databaseFile.db3");        // Create the file which will be hosting our database
using (System.Data.SQLite.SQLiteConnection con = new System.Data.SQLite.SQLiteConnection("data source=databaseFile.db3"))
{
    using (System.Data.SQLite.SQLiteCommand com = new System.Data.SQLite.SQLiteCommand(con))
    {
        con.Open();                             // Open the connection to the database
 
        com.CommandText = createTableQuery;     // Set CommandText to our query that will create the table
        com.ExecuteNonQuery();                  // Execute the query
 
        com.CommandText = "INSERT INTO MyTable (Key,Value) Values ('key one','value one')";     // Add the first entry into our database 
        com.ExecuteNonQuery();      // Execute the query
        com.CommandText = "INSERT INTO MyTable (Key,Value) Values ('key two','value value')";   // Add another entry into our database 
        com.ExecuteNonQuery();      // Execute the query
 
        com.CommandText = "Select * FROM MyTable";      // Select all rows from our database table
 
        using (System.Data.SQLite.SQLiteDataReader reader = com.ExecuteReader())
        {
            while (reader.Read())
            {
                Console.WriteLine(reader["Key"] + " : " + reader["Value"]);     // Display the value of the key and value column for every row
            }
        }
        con.Close();        // Close the connection to the database
    }
}
//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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
        */
    }
}