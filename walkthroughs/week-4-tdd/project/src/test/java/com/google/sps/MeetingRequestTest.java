// Copyright 2019 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     https://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package com.google.sps;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.List;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

/** */
@RunWith(JUnit4.class)
public final class MeetingRequestTest {
  // Some people that we can use in our tests.
  private static final String PERSON_A = "Person A";
  private static final String PERSON_B = "Person B";
  private static final String PERSON_C = "Person C";

  private static final int DURATION_1_HOUR = 60;

  @Test
  public void CantAddOptionalAttendeeWhoIsAlsoMandatory() {
    MeetingRequest request = new MeetingRequest(Arrays.asList(PERSON_A), DURATION_1_HOUR);
    request.addOptionalAttendee(PERSON_A);

    int actual = request.getOptionalAttendees().size();
    int expected = 0;
    Assert.assertEquals(expected, actual);
  }
}