import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.*;
/**
 * Created by ma on 04.03.14.
 */
public class StudentServlet extends HttpServlet {
    Connection conn;

    @Override
    public void init() throws ServletException {
        super.init();
        try {
            Class.forName("org.postgresql.Driver");
            conn = DriverManager.getConnection(
                    "jdbc:postgresql://localhost:5432/univer",
                    "postgres",
                    "postgres");
        } catch (SQLException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }

    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String task = request.getParameter("task");
        PrintWriter pw = response.getWriter();
        if (task != null) {
            if (task.equals("delete")) {
                try {
                    Statement s1 = conn.createStatement();
                    s1.execute("delete from students " +
                            "where id = " + request.getParameter("id"));
                    response.sendRedirect("/students");
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
       }
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String task = request.getParameter("task");
        PrintWriter pw = response.getWriter();
        pw.println("<!DOCTYPE html><html>" +
                "<head>" +
                "<link rel=\"stylesheet\" type=\"text/css\" " +
                "href=\"/css/bootstrap.css\">" +
                "</head><body>");
        if (task != null) {
            if (task.equals("new")) {
                pw.println("new");
            }
            else if (task.equals("delete")){
                pw.println("<h2>Deleting student</h2>");
                Statement s1= null;
                try {
                    s1 = conn.createStatement();
                    ResultSet r1 = s1.executeQuery(
                            "select * from students" +
                                    " where id=" + request.getParameter("id")
                    );
                    r1.next();
                    pw.println("<p>"+ r1.getString("fio") + "</p>");
                    pw.println("<p>"+ r1.getString("gr") + "</p>");
                    pw.println("Do you want to delete this student?");
                    pw.println("<form action='/students' method='POST'>" +
                            "<input type='hidden' name='task' value='delete'>" +
                            "<input type='hidden' name='id' value='" + r1.getString("id") + "'>" +
                            "<input type='submit' value='Delete'/>" +
                            "</form>");

                } catch (SQLException e) {
                    e.printStackTrace();
                }

            }
            else if (task.equals("edit")) {
                pw.println("edit");
            }
        }
        else {
            try {
                response.setContentType("text/html");
                Statement s1 = conn.createStatement();
                ResultSet r1 = s1.executeQuery("select * from students");
                pw.println("<table class=\"table\">");
                int k = 0;
                while (r1.next()){
                    k += 1;
                    pw.println("<tr>");
                    pw.println("<td>" + k + "</td>");
                    pw.println("<td>" + r1.getString("fio") + "</td>");
                    pw.println("<td>" + r1.getString("gr") + "</td>");
                    pw.println("<td><a href='/students?task=edit&id="+ r1.getString("id") + "'>Edit</a></td>");
                    pw.println("<td><a href='/students?task=delete&id="+ r1.getString("id") + "'>Delete</a></td>");
                    pw.println("</tr>");
                }
                pw.println("</table>");
                pw.println("<a href='/students?task=new'>New student</a>");
                pw.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
        //pw.println("</body></html>");
    }
}
