package com.wizeline;
import static com.wizeline.Methods.*;
import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

/**
 * Unit test for simple App.
 */
public class MethodsTest extends TestCase{

    public MethodsTest( String testName ){
        super( testName );
    }

    public static Test suite(){
        return new TestSuite( MethodsTest.class );
    }

    public void testGenerateToken(){
      assertEquals("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.StuYX978pQGnCeeaj2E1yBYwQvZIodyDTCJWXdsxBGI", Methods.generateToken("admin", "secret"));
    }

    public void testAccessData(){
      assertEquals("You are under protected data", Methods.accessData("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.StuYX978pQGnCeeaj2E1yBYwQvZIodyDTCJWXdsxBGI"));
    }
}
